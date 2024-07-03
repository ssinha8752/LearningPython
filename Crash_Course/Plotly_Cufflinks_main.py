import cufflinks as cf
import numpy as np
import pandas as pd
from plotly.offline import init_notebook_mode,iplot
import chart_studio.plotly as py

init_notebook_mode(connected=True)
cf.go_offline()

#DATA
df=pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[31,45,65]})

#df.iplot()#can show dynamic plots on the graph

df.iplot(kind='scatter',x='A',y='B',mode='markers')


