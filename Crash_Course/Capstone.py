import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('911.csv')

print(df.info())
#print(df['zip'].value_counts().head())

#print(df['twp'].value_counts().head())

#print(df['title'].nunique())

df['Reason']=df['title'].apply(lambda x:x.split(':')[0])
#print(df['Reason'].value_counts())

#re=df['Reason'].value_counts()
#sns.countplot(x='Reason',data=df,palette='viridis')
#plt.show()



df['timeStamp']=pd.to_datetime(df['timeStamp'])


df['Hour']=df['timeStamp'].apply(lambda x:x.hour)
df['Month']=df['timeStamp'].apply(lambda x:x.month)
df['Day of Week']=df['timeStamp'].apply(lambda x:x.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thur',4:'Fri',5:'Sat',6:'Sun'}
def get_day_from_int(day_int):
    return dmap.get(day_int)

df['Day of Week']=df['timeStamp'].apply(lambda x:get_day_from_int(x.dayofweek))


#sns.countplot(x='Month',data=df,palette='viridis')


mon=df.groupby('Month').count()
#mon['lat'].plot()

#sns.lmplot(x='Month',y='twp',data=mon.reset_index())

df['Date']=df['timeStamp'].apply(lambda x:x.date())

#df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()


dh = df.groupby(by=['Hour','Day of Week']).count()['Reason'].unstack()
sns.clustermap(dh,cmap='coolwarm')
plt.show()


