import csv
import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
monday=data.loc[0]
print(int((monday.temp*9)/5)+32)


