import csv
import xlrd
import xlsxwriter

index = 1
Time_in_years = 0
Speed = 1
Vibration_Signal1 = 2
Vibration_Signal2 = 3
Vibration_Signal3 = 4
Vibration_Signal4 = 5
Vibration_Signal5 = 6
Vibration_Signal6 = 7
Vibration_Signal7 = 8
Vibration_Signal8 = 9
Buffer_Size = 16384

workbook = xlsxwriter.Workbook('Sensors_Data1.xlsx')
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


