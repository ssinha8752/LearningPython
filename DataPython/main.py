import csv
import pandas

data=pandas.read_csv("weather_data.csv")
monday=data[data.day=="Monday"]
print(int((monday.temp*9)/5)+32)

("""data_dict=data.to_dict()
data_temp=data["temp"].to_list()
print(data["temp"].max())
""")
("""


with open("weather_data.csv") as file:
    data=csv.reader(file)
    temp=[]
    for item in data:
        print(item[1])
        if item[1]!='temp':
            temp.append(int(item[1]))

    print(temp)""")
