import random
import turtle
import pandas
from collections import Counter

new_list = [n*2 for n in range(1,5)]
print(new_list)

names = ["Asdkfbj","Foidh","Sdvuog","Sfei","Mwei"]
new=[name.upper() for name in names if len(name)>5]
print(new)

student_score={student:random.randint(1,100) for student in names}
print(student_score)

passed = {student:score for (student,score) in student_score.items() if score>20}
print(passed)

weather_c = eval(input())
weather_f={day:((temp*1.8)+32) for (day,temp) in weather_c.items()}
print(weather_f)


with open("f1.txt") as file1:
  f1=file1.read()
  f1_list=f1.strip().split('\n')
  new_f1=[int(float(item)) for item in f1_list]
  print(new_f1)

with open("f2.txt") as file2:
  f2=file2.read()
  f2_list = f2.strip().split('\n')
  new_f2 = [int(float(item)) for item in f2_list]
  print(new_f2)


result = [item for item in new_f1 if item in new_f2]
print(result)