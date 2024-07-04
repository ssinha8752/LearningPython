from chart_studio import plotly
import plotly.plotly as py
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

data = dict(type='choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text = ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar= {'title':'Colorbar Title'})

layout = dict(geo={'scope':'usa'})

map=go.Figure(data = [data],layout=layout)
iplot(map)
plt.show()