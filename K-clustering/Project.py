import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import  make_blobs
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('College_data.csv',index_col=0)

#sns.scatterplot(data=df,x='Room.Board',y='Grad.Rate',hue='Private')

g=sns.FacetGrid(data=df,hue='Private')
g=g.map(plt.hist,'Outstate',bins=20,alpha=0.7)
plt.show()

kmeans = KMeans(n_clusters=2)

kmeans.fit(df.drop('Private',axis=1))

def converter(cluster):
    if cluster=='Yes':
        return 1
    else:
        return 0

df['Cluster']=df['Private'].apply(converter)

print(confusion_matrix(df['Cluster'],kmeans.labels_))
print(classification_report(df['Cluster'],kmeans.labels_))


