student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato=pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato)

nato_dict={row.letter:row.code for (key,row) in nato.iterrows()}
print(nato_dict)
name=input().upper()
name_list=[nato_dict[letter] for letter in name]
print(name_list)
