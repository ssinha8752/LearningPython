import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2

#FUNCTIONAL
#plt.plot(x,y)
#plt.xlabel('X Label')
#plt.ylabel('Y Label')
#plt.title('Title')

#MULTIPLE PLOTS
#plt.subplot(1,2,1)
#plt.plot(x,y,'b')

#plt.subplot(1,2,2)
#plt.plot(y,x,'r')


#Object Oriented

#fig = plt.figure() #create an empty canvas
#axes1=fig.add_axes([0.2,0.1,0.7,0.7]) #starting coordinates, width, height (out of 1 as it takes it as %) to make both axis on the canvas
#axes2=fig.add_axes([0.4,0.5,0.2,0.2])

#axes1.plot(x,y) #plotting the graph
#axes1.set_title('L')
#axes2.plot(y,x)
#axes2.set_title('S')

fig,axes=plt.subplots(nrows=1,ncols=1, figsize=(1,1)) #makes the axes automatically -> nrows and cols to divide the canvas and  figsize to describe the graph of the canva
plt.tight_layout()

plt.plot(x,x**2, label='Sq')
plt.plot(x,x**3, label='Cu')

plt.legend(loc=0)

plt.show()
