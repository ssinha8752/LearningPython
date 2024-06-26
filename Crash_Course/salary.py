import pandas as pd
import numpy as np
from tabulate import tabulate

salary_file=pd.read_csv("Salaries.csv", low_memory=False)

salary_file['BasePay'] = pd.to_numeric(salary_file['BasePay'], errors='coerce')
print(salary_file['BasePay'].mean())

salary_file['OvertimePay'] = pd.to_numeric(salary_file['OvertimePay'], errors='coerce')
print(salary_file['OvertimePay'].max())

print(salary_file[salary_file.EmployeeName=='JOSEPH DRISCOLL']['JobTitle'])
print(salary_file[salary_file.EmployeeName=='JOSEPH DRISCOLL']['TotalPayBenefits'])

salary_file['TotalPayBenefits'] = pd.to_numeric(salary_file['TotalPayBenefits'], errors='coerce')
print(salary_file[salary_file['TotalPayBenefits']==salary_file['TotalPayBenefits'].max()]['EmployeeName'])

print(salary_file.iloc[salary_file['TotalPayBenefits'].argmin()]['EmployeeName'])


print(salary_file.groupby('Year').mean('BasePay')['BasePay'])

print(salary_file['JobTitle'].nunique())

print(salary_file['JobTitle'].value_counts().head(5))
print(sum(salary_file[salary_file['Year']==2013]['JobTitle'].value_counts()==1))



def contains_chief(word):
    word_lower=word.lower()
    return 'chief' in word_lower.split()

print(sum(salary_file['JobTitle'].apply(lambda x: contains_chief(x))))







