import numpy

my_list=[1,2,3] #vector
print(numpy.array(my_list))


my_list_1=[[1,2,3],[2,3,4,]] #matrice
print(numpy.array(my_list_1))


print(numpy.ones(3)) #vector with ones
print(numpy.ones((3,5))) #matrice with ones

print(numpy.zeros(4)) #vector with zeros
print(numpy.zeros((4,5))) #matrice with zeros

print(numpy.random.rand(5,5)) #only +

print(numpy.random.randn(4)) #both +/-

list=numpy.arange(10) #all number <10

print(numpy.random.randint(10)) #any number <10
print(type(numpy.random.randint(5,6,10)))# low, high, frequency


print(type(my_list),type(list))
print(list.reshape(2,5)) #changes the shape of array

print(list.max(), list.argmax())


print(my_list[0:2])#sliciing
my_list[2]=100
slice_array=list[5:]
slice_array[:]=99
print(list) #direcrtly makes changes to the main numpy array to avoid memory issue. else Specifically indicate copy method
print(numpy.array[list<99])


arr=[[1,2,3],[4,5,6],[7,8,9]]
arr_2d=numpy.array(arr)
print(arr_2d[2,2])
print(arr_2d[:2,:2])