#MAIN FILE
import os
import numpy as np 
#Own Package
import Arrowhead_SCDL as scdl

#Hyperparameter settings (NO CHANGES)
MAXLEN = 400
sparse_rate = 0.1
lrate = 1e-6
delta = 0
disCond = 'rms'
disThreshold = 0.5

#Inputs
#Input files should be located in the same folder
dfile = 'T1_traineddict.mat'  #File name containing the trained dictionary
raw_data = './Turbine1.csv'     #File name containing the raw data

#Output
destFile = 'Testing'  #File name that will contain the output

#Functions
idictm = scdl.load_dict(dfile)
seg = scdl.numb_seg(raw_data)

#The variable seg control how many signal segments are processed. Each row in the "TurbineX.csv" files is considered a signal segment
#As it is currently written it will process all the rows in the file.
#The function "numb_seg" counts the number of segments (rows) in the "TurbineX.csv" file.
#If you do not want to evaluate all rows, just replace the function with any desired value
 

seqtest, dateV, selseg, dist= scdl.MPDL_vFFT_sequential(raw_data, seg, idictm, sparse_rate, disCond, disThreshold, lrate, MAXLEN, delta, destFile)

#The function "MPDL_vFFT_sequential" evaluates all the signal segments for each one of the turbines.
#As part of the project, the only output variables of your interest would be 'dist' and 'selseg'
# The output variable 'seqtest' is the one containing all the data that is saved on an output JSON file, but I believe you can discart this output file.
#As part of the operation of the method, the algorithm does not evaluate the signal segments where the wind turbine was in iddle.
#The iddle condition is evaluated with a threshold setting (hyperparameters).
# All the signal segments (rows) that are above this threshold setting are processed with the machine learning algorithm. 
# The selected segments (rows) are saved in the output variable'selseg', with the corresponding date (signal segment time) saved in the variable 'dateV'.
# The metric which you are interested to transmit as part of the project is the output variable 'dist', this value should be transmitted with the average, rms, initial, final, etc values
# Thus, all this method is to be implemented in the local clouds of each one of the turbines.
# 
# All the functions that enable the operation of this algorithm are located in the "Arrowhead_SCDL.py" file  

