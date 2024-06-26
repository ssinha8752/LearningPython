import csv
import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
monday=data[data.day=='Monday']
print(int((monday.temp*9)/5)+32)


