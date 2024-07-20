import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
df=pd.read_csv('KNN_project.csv')

#sns.pairplot(data=df,hue='TARGET CLASS')

scaler=StandardScaler()

scaler.fit(df.drop('TARGET CLASS',axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

df_features=pd.DataFrame(scaled_features,columns=df.columns[:-1])

print(df_features.head())

X=df_features
Y=df['TARGET CLASS']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=101)

knn = KNeighborsClassifier(n_neighbors=53)

knn.fit(X_train,Y_train)

pred=knn.predict(X_test)

print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))

error_rate=[]

for i in range(1,100):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,Y_train)
    pred_i=knn.predict(X_test)
    error_rate.append(np.mean(pred_i != Y_test))

plt.figure(figsize=(12,8))
plt.plot(range(1,100),error_rate,color='red',linestyle='-',marker='o')
plt.show()