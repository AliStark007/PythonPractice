# File created to practice using Python's Numpy Library
import numpy as np
import sys

#The Basics

a= np.array([1,2,3],dtype='int16')
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

#Get Dimensions
print(a.ndim)
print(b.ndim)

#Get Shape
print(a.shape)
print(b.shape)

#Get Type
print(a.dtype)