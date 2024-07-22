import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split,GridSearchCV


can=load_breast_cancer()

df_feat=pd.DataFrame(can['data'],columns=can['feature_names'])

print(can.keys())

X=df_feat
Y=can['target']


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=101,test_size=0.33)

from sklearn.svm import SVC

model=SVC()

model.fit(X_train,Y_train)

pred=model.predict(X_test)

print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))

param = {'C':[0.1,1,10,100,100], 'gamma':[1,.1,.01,.001,.0001]}

grid=GridSearchCV(SVC(),param_grid=param,verbose=3)

grid.fit(X_train,Y_train)

grid_pred=grid.predict(X_test)

print(confusion_matrix(Y_test,grid_pred))
print(classification_report(Y_test,grid_pred))