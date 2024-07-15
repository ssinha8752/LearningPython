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

train['Fare'].hist(bins=40,figsize=(10,4))
plt.show()



