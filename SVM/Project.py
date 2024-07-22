import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.svm import SVC

iris=sns.load_dataset('iris')

#sns.pairplot(iris,hue='species')

#setosa = iris[iris['species']=='setosa']

#sns.kdeplot(x=setosa['sepal_width'],y=setosa['sepal_length'])

X=iris.drop('species',axis=1)
Y=iris['species']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=101,test_size=0.33)

svc= SVC()

svc.fit(X_train,Y_train)

pred=svc.predict(X_test)

print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))

param_grid = { 'C':[0.1,1,10,100], 'gamma':[1,0.1,0.01, 0.001]}

grid=GridSearchCV(SVC(),param_grid,verbose=3)

grid.fit(X_train,Y_train)

grid_pred= grid.predict(X_test)

print(confusion_matrix(Y_test,grid_pred))
print(classification_report(Y_test,grid_pred))









