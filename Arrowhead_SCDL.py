import os
import scipy.io
import copy
import csv
import numpy as np
import random
import time
import codecs
import json

#The below function loads a dictionary from a file
def load_dict(filename):
    mat = scipy.io.loadmat(filename)
    idictm_p = mat['idictm']
    return idictm_p

def total_atoms(dict):
    M = dict.shape[1]
    return M

def numb_seg(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 2:
                return line_count            
    return line_count

def read_seg(filename, segnum):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        rows = list(csv_reader)
    return rows[segnum]

def rms(array_vector):
        return np.sqrt(np.mean(np.square(array_vector)))

#Post-processing
def pp(array_vector):
    meanInp = np.mean(array_vector)
    stdInp = np.std(array_vector)
    PP_const = [meanInp, stdInp]
    signal = (array_vector-meanInp)/stdInp
    return signal, PP_const

def SegCond(filename, segnum, condition):
        rawrow = read_seg(filename, segnum)
        #If-else used to select the discriminant condition
        if condition == 'rms':
            value = rms(np.array(rawrow[2:]))
  
        else:
            raise Exception('This is not a valid condition selected.')

        return value

#The function creates a random input segment of one second length to be used as input to the sparse coding algorithm.
def createWDataPP(filename, segnum):
    rawrow = read_seg(filename, segnum)
    #Loading the date data
    dateV = rawrow[0]
    #Loading the MeasInfo data (speed)
    meas_info = rawrow[1]
    #Loading the Vibration signal
    VibData = np.array(rawrow[2:])
    inputSeg = np.transpose(VibData)   #Double-check if needed
    inputSeg, PPconst = pp(inputSeg)

    return inputSeg, PPconst, dateV, meas_info

def dictionary_update(d, r, e, t, w, gamma, max_len):
    ld = copy.deepcopy(d)
    M = total_atoms(d)
    for i in range(M):
        mask = np.in1d(i, e)
        if not any(mask):
            continue
            
        #Functionvariables
        atom = ld[0][i]
        alen = len(atom[0])
        grd = np.zeros(alen)
        mask = np.in1d(e,[i])  #Mask to identify the events for each atom
        pos = t[mask]
        wgt = w[mask]

        #Gradient, sum over atomic events
        for j in range(len(pos)):
            grd = grd + wgt[j]*r[ pos[j]:pos[j]+alen ]
        
        #Update and normalize
        atom = atom + gamma*(grd/np.var(r))
        atom = atom/np.linalg.norm(atom)

        #Extend atom tails if necessary
        ms = np.sum(atom[0][10:-10]**2) / len(atom[0][10:-10])
        msh = np.sum(atom[0][0:10]**2)/10
        mst = np.sum(atom[0][-10:]**2)/10
        if msh > 0.1*ms and len(atom) < max_len-10:
            atom = np.pad(atom,(10,0),'constant')
        if mst > 0.1*ms and len(atom) < max_len-10:
            atom = np.pad(atom,(0,10),'constant')
        ld[0][i] = atom

    return ld

def FFTmpdl_1D(d, x, max_e, gamma, max_len):
    '''              
    Inputs
        d:       dictionary of atoms
        x:       signal
        max_e:   max number of events    (stopping condition)
        gamma:   learning rate
        max_len: maximum length of atoms
    Outputs
        e:       atom indices of events
        t:       x offsets of events
        w:       weights of events
        r:       signal residual
        ld:      updated dictionary of atoms
        snr:     signal to residual ratio in dB
    ''' 
    #Preallocation of output variables
    M = total_atoms(d)
    x = x.flatten()
    e = [0]*max_e
    t = [0]*max_e
    w = np.zeros(max_e)
    r = copy.deepcopy(x)

    for ii in range(max_e):
        w_ind = np.zeros(M)
        t_ind = [0]*M
        for i in range(M):
            atom = d[0][i]
            alen = len(atom[0])
            slen = len(r)
            #zero-padding to have both vectors in equal length
            atom_pad = np.pad(atom[0], (0,slen+slen-alen-1),'constant')
            signal_pad = np.pad(r, (slen-1,0),'constant')
            #FFT
            atom_fft = np.fft.fft(atom_pad)
            signal_fft = np.fft.fft(signal_pad)
            #Inverse
            cc = np.fft.ifft( np.conjugate(atom_fft)*signal_fft )
            cc = cc[slen-1:-alen]
            #Max inner-product value within atom
            w_ind[i] = np.amax(cc)
            t_ind[i] = np.argmax(cc)

        # Max inner-product value within dictionary
        e[ii] = np.argmax(w_ind)
        t[ii] = t_ind[e[ii]]
        w[ii] = w_ind[e[ii]]
        #Substraction of selected atom to get new residual
        sel_atom = d[0][e[ii]]
        r[t[ii]:t[ii]+len(sel_atom[0])] = r[t[ii]:t[ii]+len(sel_atom[0])] - w[ii]*sel_atom[0]

    e = np.array(e)
    t = np.array(t)
    w = np.array(w)
        
    #Calculate Signal-to-Residual ratio
    xr = x[0:len(r)] - r
    snr = 20*np.log10(np.linalg.norm(xr)/np.linalg.norm(r))

    #Dictionary Learning
    ld = dictionary_update(d, r, e, t, w, gamma, max_len)
    
    return e, t, w, r, ld, snr

def dict_cross_padm(dictA, dictB):
    vcorr = np.zeros((1, total_atoms(dictA)))
    posB = np.zeros((1, total_atoms(dictA)))
    for i in range(total_atoms(dictA)):
        for j in range(total_atoms(dictB)):
            temp = np.correlate(np.ndarray.flatten(dictA[0][i]),np.ndarray.flatten(dictB[0][j]),"full")
            mtemp = np.amax(temp)
            if mtemp > vcorr[0,i]:
                vcorr[0,i] = mtemp
                posB[0,i] = j
    return vcorr, posB
    
def dict_dist(dictA, dictB):
    vcorr1, pos = dict_cross_padm(dictA, dictB)
    vcorr2, pos = dict_cross_padm(dictB, dictA)
    betadeg1 = np.degrees(np.arccos(vcorr1))
    betadeg2 = np.degrees(np.arccos(vcorr2))
    dist=(np.sum(betadeg1)+np.sum(betadeg2))/(total_atoms(dictA)+total_atoms(dictB))
    return dist

def dictDistSeq(ldcm, delta):
    distm = [0]*len(ldcm)
    for i in range(delta,len(ldcm)):
        if delta == 0:
            ref = 0
        else:
            ref = i-delta

        if ref == i:
            distm[i] = 0
        else:
            distm[i] = dict_dist(ldcm[ref], ldcm[i])
    return distm

def MPDL_vFFT_sequential(filename, seg, initial_dict, sparse_rate, disCond, disThreshold, lrate, MAXLEN, delta, destFile):
        #filename is the name of the input file    

        rawrow = len(read_seg(filename, 0))
        expSegL = rawrow - 2  #We substract 2 because first two columns correspond to time and speed 
        #Calculation of actual number of iterations and rounded to the closest 100
        it = int(round(sparse_rate*expSegL,-2))
        
        #Preallocation
        DBm = np.zeros([seg])
        ldcm = [initial_dict]*seg
        em = np.zeros([it,seg])
        tm = np.zeros([it,seg])
        wm = np.zeros([it,seg])
        PPconst = np.zeros([seg,2])
        dateV = []
        measInfo = []
        sel_discriminant = np.zeros([seg])   #vector to keep selected discriminant values
        all_discriminant = np.zeros([seg])   #vector to keep all discriminant values
        selseg = []

        sii = 0  #This variable controls where the info is saved

        
        for i in range(seg):
            if sii==0:
                ldcm[0] = initial_dict
            else:
                ldcm[sii] = ldcm[sii-1]
   
            t = time.time()
            all_discriminant[i] = SegCond(filename, i, disCond)
            if all_discriminant[i] < disThreshold:
                continue
            else:
                sel_discriminant[sii] = all_discriminant[i]
            iseg, PPconst[sii,:], dateVp, measInfop = createWDataPP(filename, i)
            dateV.append(dateVp)
            measInfo.append(measInfop)
            
            #Verify that iseg has always the required dimensions
            input = np.zeros([expSegL])
            if len(iseg)==len(input):
                input=copy.deepcopy(iseg)
            elif len(iseg)<len(input):
                input[0,0:len(iseg)] = copy.deepcopy(iseg)
            elif len(iseg)<len(input):
                input = copy.deepcopy(iseg[0,0:len(input)])
            
        
            etm, ttm, wtm, r, ldcm[sii], DBm[sii] = FFTmpdl_1D(ldcm[sii], input, it, lrate, MAXLEN)
            em[0:len(etm),sii] = etm
            tm[0:len(etm),sii] = ttm
            wm[0:len(etm),sii] = wtm

            selseg.append(i)
            sii += 1

            elapsed = time.time() - t
            print('Segment {} of {} is DONE in {} seconds.'.format(i+1,seg,elapsed))
        
        #Removal of elements from unselected segments
        em = em[:,0:sii]
        tm = tm[:,0:sii]
        wm = wm[:,0:sii]
        DBm = DBm[0:sii]
        ldcm = ldcm[0:sii]
        PPconst = PPconst[0:sii,:]
        measInfo = measInfo[0:sii]
        sel_discriminant = sel_discriminant[0:sii]

        print('Calculating dictionary distances, please wait a few minutes...')
        dist = dictDistSeq(ldcm, delta)
        
        ldcm2 = [l.tolist() for l in ldcm] #This is to convert each dictionary to a list
        #Since each dictionary is an object, then it is needed to go through each of them to convert to list
        ldcm3 = []
        for i in range(sii):
            templd = ldcm2[i]
            templd2 = [l.tolist() for l in templd[0]]
            ldcm3.append(templd2)

        sequential_MP = {
            #'Events' : em.tolist(),
            #'Time_shift' : tm.tolist(),
            #'Weights' : wm.tolist(),
            #'SNR' : DBm.tolist(),
            'Learned_Dictionary' : ldcm3,
            'Initial_Disctionary' : [l.tolist() for l in initial_dict[0]], #initial_dict,
            #'Turbine' : turb,
            #'PP_constants' : PPconst.tolist(),
            'Date' : dateV,#dateV,
            'Measurement_Info' : measInfo,#[l.tolist() for l in measInfo],#measInfo,
            'Selected_Segments' : selseg,
            'All_Discriminant' : all_discriminant.tolist(), #this is the RMS value of all segments
            #'Selected_Discriminant' : sel_discriminant.tolist(),
            #'Learning_Rate' : lrate,
            #'Max_Length' : MAXLEN,
            'Dictionary_distance': dist,
        }
        #with open(destFile+'.json', 'w') as fp:
        json.dump(sequential_MP, codecs.open(destFile+'.json', 'w', encoding='utf-8'))

        #return DBm,ldcm,em,tm,wm,inpin,PPconst,dateV,measInfo,discriminant,turb,initial_dict,lrate,MAXLEN
        return sequential_MP, dateV, selseg, dist