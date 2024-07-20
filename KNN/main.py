import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

df=pd.read_csv('Classifies_data.csv',index_col=0)


scaler = StandardScaler()

scaler.fit(df.drop('TARGET CLASS',axis=1))

scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

df_feat=pd.DataFrame(scaled_features,columns=df.columns[:-1])


X = df_feat
Y = df['TARGET CLASS']
X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=101)

knn=KNeighborsClassifier(n_neighbors=36)

knn.fit(X_train,Y_train)

pred = knn.predict((X_test))

print(confusion_matrix(Y_test,pred))
print(classification_report(Y_test,pred))

error_rate=[]

for i in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,Y_train)
    pred_i=knn.predict(X_test)
    error_rate.append(np.mean(pred_i != Y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o')
plt.show()

