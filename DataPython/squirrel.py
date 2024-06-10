import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color=data["Primary Fur Color"]
g=0
r=0
b=0
count_sq={
    "color":["Gray","Red","Black"],
    "count":[g,r,b]
}
for i in color:
    if i=="Gray":
        count_sq["count"][0]+=1
    elif i == "Cinnamon":
        count_sq["count"][1]+=1
    elif i == "Black":
        count_sq["count"][2]+=1

new_count=pandas.DataFrame(count_sq)
print(new_count)