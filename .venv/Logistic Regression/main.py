import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

train=pd.read_csv("titanic_train.csv")
test=pd.read_csv("titanic_test.csv")

#sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

sns.set_style('whitegrid')
#sns.countplot(x='Survived',data=train,hue='Pclass')
#sns.displot(train['Age'].dropna(),kde=False,bins=30)

#sns.countplot(x='SibSp',data=train)

#train['Fare'].hist(bins=40,figsize=(10,4))
#sns.boxplot(x='Pclass',y='Age',data=train)

def impute_age(cols):
    a=cols.iloc[0]
    p=cols.iloc[1]

    if pd.isnull(a):
        if p==1:
            return 37
        elif p==2:
            return 29
        else:
            return 24
    else:
        return a

train['Age']=train[['Age','Pclass']].apply(impute_age,axis=1)
#sns.heatmap(data=train.isnull(),yticklabels=False,cmap='viridis',cbar=False)

train.drop('Cabin',axis=1,inplace=True)
train['Age']=train[['Age','Pclass']].apply(impute_age,axis=1)
sns.heatmap(data=train.isnull(),yticklabels=False,cmap='viridis',cbar=False)


sex=pd.get_dummies(train['Sex'],drop_first=True)
emb=pd.get_dummies(train['Embarked'],drop_first=True)
train=pd.concat([train,sex,emb],axis=1)

train.drop(['Sex','Embarked','Name','Ticket','PassengerId'], axis=1,inplace=True)

X=train.drop('Survived',axis=1)
Y=train['Survived']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.33, random_state=101)


logmodel = LogisticRegression()

logmodel.fit(X_train,Y_train)

lm = LinearRegression()

lm.fit(X_train,Y_train)

predictions = logmodel.predict((X_test))

print(confusion_matrix(Y_test,predictions))




