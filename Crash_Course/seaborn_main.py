import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
print(tips.head())

#Histogram
#sns.displot(tips['total_bill'])

#Scatter Plot
#sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')
#plt.show()

#Pairplot for all numerical column values
#sns.pairplot(tips,hue='sex') #hue is for categorical column
#plt.show()

#rugplot marka dash plot throughout the single line
#sns.rugplot(tips['total_bill'])
#plt.show()

#barplot
#sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)

#count_plot
#sns.countplot(x='sex',data=tips)

#candlecharts
#sns.boxplot(x='day',y='total_bill',data=tips)

#violinplot
#sns.violinplot(x='day',y='total_bill', data=tips, hue='sex')

#stripplot
#sns.stripplot(x='day',y='total_bill',data=tips, jitter=True)


#stripplot + violin
#sns.swarmplot(x='day',y='total_bill',data=tips)

#df=pd.DataFrame(tips)

#pivot_table = df.pivot_table(index='sex', columns='day', values='total_bill', aggfunc='sum')

# Create heatmap
#plt.figure(figsize=(10, 6))
#sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='.2f')

# Set titles and labels
#plt.title('Total Bill Heatmap')
#plt.xlabel('Day')
#plt.ylabel('Sex')

#df=pd.DataFrame(flights)

#pivot_table = df.pivot_table(index='month', columns='year', values='passengers')
#sns.heatmap(pivot_table)

#sns.clustermap(pivot_table)
#plt.show()

iris = sns.load_dataset('iris')
#print(iris.head())

#print(iris.species.unique())

#g = sns.PairGrid(iris) #shows empty pairGrid
#g.map_diag(sns.displot) #maps through the diagnoal of the pairgrid
#g.map_upper(plt.scatter) #maps through the upper half of the diagnoal
#g.map_lower(sns.kdeplot)# maps through the lower half of the diagnoal

#g=sns.FacetGrid(data=tips,col='time',row='smoker') #make grids for specified rows and cols
#g.map(sns.displot,'total_bill') #create the graph as per the rows and columns



sns.lmplot(data=tips,x='total_bill',y='tip',col='sex')#Linear regression
plt.show()



