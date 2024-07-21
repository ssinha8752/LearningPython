import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

loans=pd.read_csv('loan_data.csv')

#loans[loans['not.fully.paid']==1]['fico'].hist(color='red')
#loans[loans['not.fully.paid']==0]['fico'].hist(color='blue')

#plt.figure(figsize=(11,7))
#sns.countplot(data=loans,x='purpose',hue='not.fully.paid')

#sns.jointplot(x='fico',y='int.rate',data=loans)

#sns.lmplot(y='int.rate',x='fico',data=loans, hue='credit.policy')

cf=['purpose']

fd=pd.get_dummies(loans,columns=cf,drop_first=True)

X=fd.drop('not.fully.paid',axis=1)
Y=fd['not.fully.paid']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

dtree= DecisionTreeClassifier()

dtree.fit(X_train,Y_train)

pred=dtree.predict((X_test))

print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))

rfc= RandomForestClassifier(n_estimators=300)

rfc.fit(X_train,Y_train)

predictions = rfc.predict(X_test)

print(confusion_matrix(Y_test,predictions))
print(classification_report(Y_test,predictions))

