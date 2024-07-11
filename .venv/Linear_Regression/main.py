import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv('USA_Housing.csv')

df1=df.drop(columns=['Address'])



X = df1[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

Y = df1['Price']

X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.4, random_state=101)

lm = LinearRegression()

lm.fit(X_train,Y_train)

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])

pred = lm.predict(X_test)

#plt.scatter(Y_test,pred)

snb.displot((Y_test-pred))
plt.show()