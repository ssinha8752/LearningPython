import numpy.random as np
import numpy as nm
import pandas as pd

#series
#based on array, but also renders the index and can store variety of object types

l=['a','b','v']
n=[1,2,3]
print(pd.Series(data=l, index=n)) #index is optional

ser_1=pd.Series(data=l, index=n)
print(ser_1[1]) #a


#Data Frames
df = pd.DataFrame(np.rand(5,4),[1,2,3,4,5],['A','B','C','D'])
print(df)
print(df['A']) #extracting a column
print(df.A)#extracting a column

print(df[['A','B']]) #extracting multiple columns

df['E']=df['A']+df['B'] #adding new column
print(df)

df.drop('E', axis=1, inplace=True) #removing a column (axis=1) row(axis=0) inplace = True to drop the column permenantly

print(df.loc[1]) #extracting row based on name of the index
print(df.iloc[0]) #extracting row based on the index

print(df.loc[1,'B']) #extracting a cell

print(df[df>0.5]) #df>0.5 will be boolean and values will be NaN where they are false

print(df['A']>0.7) #output will be true or false
print(df[df['A']>0.7]) #output will be only rows which are true

print(df[df['A']>0.7][['B','C']]) #only for the column of B and C

print(df[(df['A']>0.5) & (df['C']>0.5)]) # returns the row for which both the condition is true

print(df.reset_index()) #reset index
print(df.set_index('A')) #set_index  as per particular column

print(df)

o=['G1','G1','G1','G2','G2','G2']
i=[1,2,3,1,2,3]
hier_index=list(zip(o,i)) #create tuples (G1,1) etc

hierindex1=pd.MultiIndex.from_tuples(hier_index)

print(hierindex1)

df= pd.DataFrame(np.randn(6,2),hierindex1,['A','B'])
print(df)

print(df.loc['G1'].loc[1])

df.index.names = ['Groups','Num'] #Add names to index
print(df.xs(1,level='Num')) #Extract num=1


#Missing Values
d={'A':[1,2,nm.nan],'B':[3,4,nm.nan],'C':[1,2,3]}
df=pd.DataFrame(d)
print(df)

print(df.dropna(thresh=2)) #only shows rows without NA/ Thresh=2 would shows those rows with atleast 2 values in it

print(df.fillna(value=2)) #fills NaN with value


#GroupBy
data={
    'Company':['A','A','B','C','C'],
    'Person':['D','E','F','G','H'],
    'Sales':[145,200,432,345,356]
}

df=pd.DataFrame(data)
comp=df.groupby('Company')
print(comp.mean('Sales'))
print(comp.describe().transpose()['B'])


#Operations
print(df['Company'].unique()) #A,B,C
print(df['Company'].nunique()) #3
print(df['Company'].value_counts()) #Frequency Counter

def time2(x):
    return x*2

print(df['Sales'].apply(time2))
print(df['Sales'].apply(lambda x:x*2))

print(df.isnull())

print(df.pivot_table(values='Sales',index=['Company','Person'],columns=['Person']))