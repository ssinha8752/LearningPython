import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers=pd.read_csv('Ecomm_Customers_Sample.csv')

#sns.jointplot(customers,x='Time on App',y='Length of Membership',kind='hex')

#sns.pairplot(customers)

#sns.lmplot(data=customers,x='Yearly Amount Spent',y='Length of Membership')
#plt.show()

print(customers.columns)

X=customers[['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']]
Y=customers['Yearly Amount Spent']

X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=101)

lm=LinearRegression()

lm.fit(X_train,Y_train)

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])

pred = lm.predict(X_test)

sns.scatterplot(x=Y_test,y=pred)

print('MSE',metrics.mean_squared_error(Y_test,pred))
print('MAE',metrics.mean_absolute_error(Y_test,pred))
print('RMSE',metrics.root_mean_squared_error(Y_test,pred))

print('Var',metrics.explained_variance_score(Y_test,pred))




