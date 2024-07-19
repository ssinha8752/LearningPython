import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


ad_data=pd.read_csv('advertising.csv')

#sns.jointplot(data=ad_data,y='Daily Internet Usage',x='Daily Time Spent on Site')

#sns.pairplot(data=ad_data,hue='Clicked on Ad')
#plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

X=ad_data[['Daily Time Spent on Site','Age','Daily Internet Usage','Area Income','Male']]
Y=ad_data['Clicked on Ad']

X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=101)


logmodel = LogisticRegression()

logmodel.fit(X_train,Y_train)

predictions = logmodel.predict((X_test))

print(classification_report(Y_test,predictions))