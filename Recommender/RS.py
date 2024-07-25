import numpy as np
import pandas as pd

columns_names = ['user_id','item_id','rating','timestamp']

df=pd.read_csv('u.data', sep='\t',names=columns_names)

movie_titles = pd.read_csv('Movie_ID.csv')

df=pd.merge(df,movie_titles,on='item_id')

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')

ratings=pd.DataFrame(df.groupby('title')['rating'].mean())

ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

#ratings['rating'].hist(bins=70)

sns.jointplot(x='rating',y='num of ratings',data=ratings)
plt.show()

