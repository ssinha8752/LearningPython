import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix


df= pd.read_csv('kyphosis.csv')

sns.pairplot(df,hue='Kyphosis')

X=df.drop('Kyphosis',axis=1)
Y=df['Kyphosis']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

Dtree=DecisionTreeClassifier()

Dtree.fit(X_train,Y_train)

pred=Dtree.predict((X_test))


rfc=RandomForestClassifier()

rfc.fit(X_train,Y_train)

prediction=rfc.predict((X_test))

print(confusion_matrix(Y_test,prediction))
print(classification_report(Y_test,prediction))