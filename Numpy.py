import numpy as np


#Numpy is multidimensional array and faster than list
#This is how vector and matrices are created using numpy
a=np.array([1,2,3])
b=np.array([ [1.0,2.0,3.0],[4.0,5.0,6.0] ])
print("a vector is",a)
print("b matrix is \n",b)


#dimension of array by ndim
#rows x column by shape function.
print(a.ndim) #1 dimensional
print(b.ndim) #2 dimensional
print(a.shape) # (3,) for 3 columns
print(b.shape) #(2,3) 2 rows 3 columns

#Get Type
print("datatype of a ",a.dtype)
#redefining 'a' to have a particular datatype and itemsize
a=np.array([1,2,3,4],dtype="int16")
print("datatype of a ",a.dtype)
print("datatype of b ",b.dtype,"\n")

#Get size
print("Size of each item in a:",a.itemsize)
print("Total Size of a:",a.nbytes)
print("No. of elements in a:",a.size,"\n")

print("Size of each item in b:",b.itemsize)
print("Total Size of b:",b.nbytes)
print("No. of elements in b:",b.size,"\n\n")

""""

ACESSING ARRAY ELEMENTS AND THEIR MANIPULATION
a[row,column] gives the apecific element.

"""
a=np.array([[1,2,3,4],[4,5,6,7]],dtype="int32")
print(a)
print("a[second row,third column]:",a[1,2])


