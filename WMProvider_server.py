from flask import Flask, jsonify
from http.server import CGIHTTPRequestHandler, HTTPServer

#from flask_restful import Api, Resource, reqparse
import random
import csv
import xlrd
import xlsxwriter
import os
import numpy as np
import requests
import json
#Own Package
import Arrowhead_SCDL as scdl

#Arrowhead URLS

serviceRegisteryURL = "http://localhost:8443/"
authorizationURL = "http://localhost:8445/"
orchestratorURL = "http://localhost:8441/"


app = Flask(__name__)
#api = Api(app)

Sensors_Data = [
     {'id': 1,
     'title': 'Sensors Data Computed by Provider',
  
      'Sensor#1 Outputs': 'SPEED',
      'Average Values': 'Sensors_Data' }
]

output_data = [
       {'id': 1,
     'title': 'Sensors Data Computed by Provider',
  
      'Sensor#1 Outputs': 'SPEED',
      'Average Values': 'Sensors_Data' }

]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Service Provider</h1>'''

@app.route('/analytics/average', methods=['GET'])
def api_all():
    Time_in_years = 0
    index = 1
    Speed = 1
    Vibration_Signal1 = 2
    Vibration_Signal2 = 3
    Vibration_Signal3 = 4
    Vibration_Signal4 = 5
    Vibration_Signal5 = 6
    Vibration_Signal6 = 7
    Vibration_Signal7 = 8
    Vibration_Signal8 = 9

    workbook = xlsxwriter.Workbook('Sensors_Data_Server.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "Time in Years")
    worksheet.write(0, 1, "Speed")
    worksheet.write(0, 2, "Vibration Signal 1")
    worksheet.write(0, 3, "Vibration Signal 2")
    worksheet.write(0, 4, "Vibration Signal 3")
    worksheet.write(0, 5, "Vibration Signal 4")
    worksheet.write(0, 6, "Vibration Signal 5")
    worksheet.write(0, 7, "Vibration Signal 6")
    worksheet.write(0, 8, "Vibration Signal 7")
    worksheet.write(0, 9, "Vibration Signal 8")

    with open("Turbine1.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            print(lines[0])
            value_Time = lines[0]
            value_Speed = lines[1]
            value_Vibration_Signal1 = lines[2]
            value_Vibration_Signal2 = lines[3]
            value_Vibration_Signal3 = lines[4]
            value_Vibration_Signal4 = lines[5]
            value_Vibration_Signal5 = lines[6]
            value_Vibration_Signal6 = lines[7]
            value_Vibration_Signal7 = lines[8]
            value_Vibration_Signal8 = lines[9]

            worksheet.write(index, Time_in_years, value_Time)
            worksheet.write(index, Speed, value_Speed)
            worksheet.write(index, Vibration_Signal1, value_Vibration_Signal1)
            worksheet.write(index, Vibration_Signal2, value_Vibration_Signal2)
            worksheet.write(index, Vibration_Signal3, value_Vibration_Signal3)
            worksheet.write(index, Vibration_Signal4, value_Vibration_Signal4)
            worksheet.write(index, Vibration_Signal5, value_Vibration_Signal5)
            worksheet.write(index, Vibration_Signal6, value_Vibration_Signal6)
            worksheet.write(index, Vibration_Signal7, value_Vibration_Signal7)
            worksheet.write(index, Vibration_Signal8, value_Vibration_Signal8)
            index += 1

    print("Final Value of Index is ", index)
    workbook.close()
    
    book = xlrd.open_workbook("Sensors_Data_Server.xlsx")
    sheet = book.sheet_by_index(0)
    header_dict = {}

    # computing values of Column 1 - Speed
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)
    maxSpeed = max(cv)
    minSpeed = min(cv)
    iniSeg_Speed = cv[0]
    endSeg_Speed = cv[(cv.__len__()-1)]

    avgSpeed = (float(maxSpeed) + float(minSpeed))/2
    print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
    print("---- Sensor#1 Outputs: SPEED ---- ")
    print("Average Speed Value is: ", avgSpeed)
    print("Maximum Speed Value is: ", maxSpeed)
    print("Minimum Speed Value is: ", minSpeed)
    print("Initial Segment Value is: ", iniSeg_Speed)
    print("End Segment Value is: ", endSeg_Speed)

    # computing values of Column 2 - Vibration Signal 1
    cv = sheet.col_values(2, start_rowx=1, end_rowx=None)
    maxVS1 = max(cv)
    minVS1 = min(cv)
    avgVS1 = (float(maxVS1) + float(minVS1))/2
    iniSeg_VS1 = cv[0]
    endSeg_VS1 = cv[(cv.__len__()-1)]
    print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
    print("---- Sensor#2 Outputs: Vibration Signal 1 ---- ")
    print("Average Vibration Signal#1 Value is: ", avgVS1)
    print("Maximum Vibration Signal#1 Value is: ", maxVS1)
    print("Minimum Vibration Signal#1 Value is: ", minVS1)
    print("Initial Segment Value is: ", iniSeg_VS1)
    print("End Segment Value is: ", endSeg_VS1)

    # computing values of Column 3 - Vibration Signal 2
    cv = sheet.col_values(3, start_rowx=1, end_rowx=None)
    maxVS2 = max(cv)
    minVS2 = min(cv)
    avgVS2 = (float(maxVS2) + float(minVS2))/2
    iniSeg_VS2 = cv[0]
    endSeg_VS2 = cv[(cv.__len__()-1)]
    print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
    print("---- Sensor#2 Outputs: Vibration Signal 2 ---- ")
    print("Average Vibration Signal#1 Value is: ", avgVS2)
    print("Maximum Vibration Signal#1 Value is: ", maxVS2)
    print("Minimum Vibration Signal#1 Value is: ", minVS2)
    print("Initial Segment Value is: ", iniSeg_VS2)
    print("End Segment Value is: ", endSeg_VS2)

    # computing values of Column 4 - Vibration Signal 3
    cv = sheet.col_values(4, start_rowx=1, end_rowx=None)
    maxVS3 = max(cv)
    minVS3 = min(cv)
    avgVS3 = (float(maxVS3) + float(minVS3))/2
    iniSeg_VS3 = cv[0]
    endSeg_VS3 = cv[(cv.__len__()-1)]
    print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
    print("---- Sensor#2 Outputs: Vibration Signal 3 ---- ")
    print("Average Vibration Signal#1 Value is: ", avgVS3)
    print("Maximum Vibration Signal#1 Value is: ", maxVS3)
    print("Minimum Vibration Signal#1 Value is: ", minVS3)
    print("Initial Segment Value is: ", iniSeg_VS3)
    print("End Segment Value is: ", endSeg_VS3)

    # computing values of Column 5 - Vibration Signal 4
    cv = sheet.col_values(5, start_rowx=1, end_rowx=None)
    maxVS4 = max(cv)
    minVS4 = min(cv)
    avgVS4 = (float(maxVS4) + float(minVS4))/2
    iniSeg_VS4 = cv[0]
    endSeg_VS4 = cv[(cv.__len__()-1)]
    print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
    print("---- Sensor#2 Outputs: Vibration Signal 4 ---- ")
    print("Average Vibration Signal#1 Value is: ", avgVS4)
    print("Maximum Vibration Signal#1 Value is: ", maxVS4)
    print("Minimum Vibration Signal#1 Value is: ", minVS4)
    print("Initial Segment Value is: ", iniSeg_VS4)
    print("End Segment Value is: ", endSeg_VS4)

    # computing values of Column 6 - Vibration Signal 5
    cv = sheet.col_values(6, start_rowx=1, end_rowx=None)
    maxVS5 = max(cv)
    minVS5 = min(cv)
    avgVS5 = (float(maxVS5) + float(minVS5))/2
    iniSeg_VS5 = cv[0]
    endSeg_VS5 = cv[(cv.__len__()-1)]
    print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
    print("---- Sensor#2 Outputs: Vibration Signal 5 ---- ")
    print("Average Vibration Signal#1 Value is: ", avgVS5)
    print("Maximum Vibration Signal#1 Value is: ", maxVS5)
    print("Minimum Vibration Signal#1 Value is: ", minVS5)
    print("Initial Segment Value is: ", iniSeg_VS5)
    print("End Segment Value is: ", endSeg_VS5)
    print("------------ ¤¤ ALL SENSOR VALUES DISPLAYED ¤¤------------------")

    # writing outputs into an xlsx file
    workbook = xlsxwriter.Workbook('Provider_Output_Analytics.xlsx')
    worksheet = workbook.add_worksheet()

    # setting labels on each row
    worksheet.write(1, 0, "Average Value")
    worksheet.write(2, 0, "Maximum Value")
    worksheet.write(3, 0, "Minimum Value")
    worksheet.write(4, 0, "Initial Segment Value")
    worksheet.write(5, 0, "End Segment Value")

    # setting lables on each column
    worksheet.write(0, 1, "Speed")
    worksheet.write(0, 2, "Vibration Signal 1")
    worksheet.write(0, 3, "Vibration Signal 2")
    worksheet.write(0, 4, "Vibration Signal 3")
    worksheet.write(0, 5, "Vibration Signal 4")
    worksheet.write(0, 6, "Vibration Signal 5")

    worksheet.write(1,1,avgSpeed)
    worksheet.write(2,1,maxSpeed)
    worksheet.write(3,1,minSpeed)
    worksheet.write(4,1,iniSeg_Speed)
    worksheet.write(5,1,endSeg_Speed)

    worksheet.write(1,2,avgVS1)
    worksheet.write(2,2,maxVS1)
    worksheet.write(3,2,minVS1)
    worksheet.write(4,2,iniSeg_VS1)
    worksheet.write(5,2,endSeg_VS1)

    worksheet.write(1,3,avgVS2)
    worksheet.write(2,3,maxVS2)
    worksheet.write(3,3,minVS2)
    worksheet.write(4,3,iniSeg_VS2)
    worksheet.write(5,3,endSeg_VS2)

    worksheet.write(1,4,avgVS3)
    worksheet.write(2,4,maxVS3)
    worksheet.write(3,4,minVS3)
    worksheet.write(4,4,iniSeg_VS3)
    worksheet.write(5,4,endSeg_VS3)

    worksheet.write(1,5,avgVS4)
    worksheet.write(2,5,maxVS4)
    worksheet.write(3,5,minVS4)
    worksheet.write(4,5,iniSeg_VS4)
    worksheet.write(5,5,endSeg_VS4)

    worksheet.write(1,6,avgVS5)
    worksheet.write(2,6,maxVS5)
    worksheet.write(3,6,minVS5)
    worksheet.write(4,6,iniSeg_VS5)
    worksheet.write(5,6,endSeg_VS5)
    workbook.close()
            
    Sensors_Data = 'Speed Values:' , avgSpeed, maxSpeed, minSpeed , iniSeg_Speed, endSeg_Speed , ' -----------' , 'Vibration Signal 1 Values:' , avgVS1 , maxVS1 , minVS1 , iniSeg_VS1 , endSeg_VS1 , ' -----------' , 'Vibration Signal 2 Values:' , avgVS2 , maxVS2 , minVS2 , iniSeg_VS2 , endSeg_VS2 , ' -----------' , 'Vibration Signal 3 Values:' , avgVS3 , maxVS3 , minVS3 , iniSeg_VS3 , endSeg_VS3 , ' -----------' , 'Vibration Signal 4 Values:' , avgVS4 , maxVS4 , minVS4 , iniSeg_VS4 , endSeg_VS4 , ' -----------' , 'Vibration Signal 5 Values:' , avgVS5 , maxVS5 , minVS5 , iniSeg_VS5 , endSeg_VS5

    return jsonify(Sensors_Data)


@app.route('/analytics/ml', methods=['GET'])
def api_ml():
    
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
           
 book = xlrd.open_workbook("Provider_Output_Analytics.xlsx")
 sheet = book.sheet_by_index(0)
 header_dict = {}

 maxSpeed = 0
 minSpeed = 0
 avgSpeed = 0
 iniSeg_Speed = 0
 endSeg_Speed = 0
 maxVs1 = 0
 minVS1 = 0
 avgVS1 = 0
 iniSeg_VS1 = 0
 endSeg_VS1 = 0

 # computing values of Column 1 - Speed
 sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

 cv = sheet.col_values(2, start_rowx=2, end_rowx=None)
 maxSpeed = max(cv)
 minSpeed = min(cv)
 avgSpeed = (float(maxSpeed) + float(minSpeed))/2
 iniSeg_Speed = cv[0]
 endSeg_Speed = cv[(cv.__len__()-1)]

 # computing values of Column 2 - Vibration Signal 1
 cv = sheet.col_values(3, start_rowx=2, end_rowx=None)
 maxVS1 = max(cv)
 minVS1 = min(cv)
 avgVS1 = (float(maxSpeed) + float(minSpeed))/2
 iniSeg_VS1 = cv[0]
 endSeg_VS1 = cv[(cv.__len__()-1)]

 Output_Data = {'Speed_Values':{
     'Average':avgSpeed,
     'Minimum':minSpeed,
     'Maximum':maxSpeed,
     'Initial_Segment':iniSeg_Speed,
     'End_Segment':endSeg_Speed 
     },
     'Vibration_Signal_Values':{
     'Average':avgVS1,
     'Minimum':minVS1,
     'Maximum':maxVS1,
     'Initial_Segment':iniSeg_VS1,
     'End_Segment':endSeg_VS1 }
 }

 Output_json = jsonify(Output_Data)

 with open('ML_Analytics_Output.json', 'w') as write_file:
    json.dump(Output_Data, write_file)

 return Output_json

@app.route('/register', methods=['GET'])
def api_sr(): 
   data = {
   "serviceDefinition": "MLProviderService8", 
   "providerSystem": 
   {
      "systemName": "MLProvider", 
      "address": "localhost", 
      "port": 5000
   },
   "serviceUri": "mlproviderservice",
   "secure":"NOT_SECURE",
   "interfaces": [
      "HTTPS-INSECURE-JSON" 
      ]
   }
   print(data) 
   # sending post request and saving response as response object 
   print(serviceRegisteryURL+'serviceregistry/register')
   r = requests.post(url = serviceRegisteryURL+'serviceregistry/register', json= data) 
   print(r.status_code)
   print(r.json)
   status=""
   if r.status_code != 201:
      print('Service Registration Failed')
      status="failed"
   else:
      print('Service Got Registered Successful')
      status="success"
   return (r.content)


app.run(debug=True)

