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

#sns.jointplot(x='rating',y='num of ratings',data=ratings)

moviemat=df.pivot_table(index='user_id',columns='title',values='rating')
#print(ratings.sort_values('num of ratings',ascending=False))

sw_ratings = moviemat['Star Wars (1977)']
ll_ratings = moviemat['Liar Liar (1997)']

sw_similar=moviemat.corrwith(sw_ratings)
ll_similar=moviemat.corrwith(ll_ratings)

corr_sw=pd.DataFrame(sw_similar,columns=['Correlation'])
corr_ll=pd.DataFrame(ll_similar,columns=['Correlation'])

corr_sw=corr_sw.join(ratings['num of ratings'])
corr_sw[corr_sw['num of ratings']>100].sort_values('Correlation',ascending=False).head()

print(corr_sw[corr_sw['num of ratings']>100].sort_values('Correlation',ascending=False).head())

corr_ll=corr_ll.join(ratings['num of ratings'])
print(corr_ll[corr_ll['num of ratings']>200].sort_values('Correlation',ascending=False).head())

