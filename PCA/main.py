import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.datasets import load_breast_cancer

C=load_breast_cancer()



df=pd.DataFrame(C['data'],columns=C['feature_names'])


print(df.head())

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

sc.fit(df)

scd=sc.transform(df)

#PCA
from sklearn.decomposition import PCA

pca=PCA(n_components=2)

pca.fit(scd)

x_pca = pca.transform(scd)

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=C['target'])
plt.show()

