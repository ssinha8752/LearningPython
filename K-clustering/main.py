import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import  make_blobs
from sklearn.cluster import KMeans

data = make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8,random_state=101)

plt.scatter(data[0][:,0],data[0][:,1],c=data[1])

K=KMeans(n_clusters=4)

K.fit(data[0])

fig, (ax1,ax2) = plt.subplots(1,2,sharey=True,figsize=(10,6))

ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=K.labels_,cmap='rainbow')

ax2.set_title('Original')
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')
plt.show()
