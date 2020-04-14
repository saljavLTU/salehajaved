# provides the output values
import xlrd
import xlsxwriter

book = xlrd.open_workbook("Sensors_Data1.xlsx")
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

# computing values of Column 7 - Vibration Signal 6
cv = sheet.col_values(7, start_rowx=1, end_rowx=None)
maxVS6 = max(cv)
minVS6 = min(cv)
avgVS6 = (float(maxVS6) + float(minVS6))/2
iniSeg_VS6 = cv[0]
endSeg_VS6 = cv[(cv.__len__()-1)]
print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
print("---- Sensor#2 Outputs: Vibration Signal 6 ---- ")
print("Average Vibration Signal#1 Value is: ", avgVS6)
print("Maximum Vibration Signal#1 Value is: ", maxVS6)
print("Minimum Vibration Signal#1 Value is: ", minVS6)
print("Initial Segment Value is: ", iniSeg_VS6)
print("End Segment Value is: ", endSeg_VS6)

# computing values of Column 8 - Vibration Signal 7
cv = sheet.col_values(8, start_rowx=1, end_rowx=None)
maxVS7 = max(cv)
minVS7 = min(cv)
avgVS7 = (float(maxVS7) + float(minVS7))/2
iniSeg_VS7 = cv[0]
endSeg_VS7 = cv[(cv.__len__()-1)]
print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
print("---- Sensor#2 Outputs: Vibration Signal 7 ---- ")
print("Average Vibration Signal#1 Value is: ", avgVS7)
print("Maximum Vibration Signal#1 Value is: ", maxVS7)
print("Minimum Vibration Signal#1 Value is: ", minVS7)
print("Initial Segment Value is: ", iniSeg_VS7)
print("End Segment Value is: ", endSeg_VS7)

# computing values of Column 9 - Vibration Signal 8
cv = sheet.col_values(9, start_rowx=1, end_rowx=None)
maxVS8 = max(cv)
minVS8 = min(cv)
avgVS8 = (float(maxVS8) + float(minVS8))/2
iniSeg_VS8 = cv[0]
endSeg_VS8 = cv[(cv.__len__()-1)]
print("------------ ¤¤ SENSOR VALUES ¤¤------------------")
print("---- Sensor#2 Outputs: Vibration Signal 8 ---- ")
print("Average Vibration Signal#1 Value is: ", avgVS8)
print("Maximum Vibration Signal#1 Value is: ", maxVS8)
print("Minimum Vibration Signal#1 Value is: ", minVS8)
print("Initial Segment Value is: ", iniSeg_VS8)
print("End Segment Value is: ", endSeg_VS8)
print("------------ ¤¤ ALL SENSOR VALUES DISPLAYED ¤¤------------------")

# writing outputs into an xlsx file
workbook = xlsxwriter.Workbook('Sensors_Output_Values.xlsx')
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
worksheet.write(0, 7, "Vibration Signal 6")
worksheet.write(0, 8, "Vibration Signal 7")
worksheet.write(0, 9, "Vibration Signal 8")

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

worksheet.write(1,7,avgVS6)
worksheet.write(2,7,maxVS6)
worksheet.write(3,7,minVS6)
worksheet.write(4,7,iniSeg_VS6)
worksheet.write(5,7,endSeg_VS6)

worksheet.write(1,8,avgVS7)
worksheet.write(2,8,maxVS7)
worksheet.write(3,8,minVS7)
worksheet.write(4,8,iniSeg_VS7)
worksheet.write(5,8,endSeg_VS7)

worksheet.write(1,9,avgVS8)
worksheet.write(2,9,maxVS8)
worksheet.write(3,9,minVS8)
worksheet.write(4,9,iniSeg_VS8)
worksheet.write(5,9,endSeg_VS8)

workbook.close()