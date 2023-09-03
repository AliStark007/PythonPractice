# File created to practice using Python's Numpy Library
import random

import numpy as np
import sys

# The Basics

a = np.array([1, 2, 3], dtype='int16')
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

# Get Dimensions
print(a.ndim)
print(b.ndim)
# Get Shape
print(a.shape)
print(b.shape)
# Get Type
print(a.dtype)
# Get Size
a.itemsize
a.size
# Get Total Size
print(a.size * a.itemsize)
print(a.nbytes)

# Accessing/Changing Specific elements
c = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# Get a specific element
print(c[1, 5])  # Python indexing starts at 0
print(c[1, -2])  # Can index from back starting with 1
# Get a specific row
c[0, :]
c[:, 1]
# Getting fancy [startindex:endindex:stepsize]
c[0, 1:6:2]  # End index element is excluded like in range
c[0, 1:-1:2]
# Changing element/s
c[1, 5] = 20
c[:, 2] = 5
c[:, 2] = [1, 2]
# 3D Example
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
d[0, 1, 0]  # Work outside in to access elements
d[:, 1, :]
d[:, 1, :] = [[9, 9], [8, 8]]  # Easy as long as dimensions are consistent

# Initializing different types of array
#All 0s matrix
np.zeros(5)
np.zeros((2,3))
#All 1s matrix
np.ones((4,2,2),dtype='int32')
#Any other number
np.full((2,2),99,dtype='float32')
#full_like method
np.full_like(c,4)
#Random decimal numbers
np.random.rand(4,2,3)
#Random sample allows us to pass shape
np.random.sample(c.shape)
#Random integer values
np.random.randint(7,size=(3,3)) #Note this is assigned to size instead of shape
np.random.randint(4,7,size=(3,3)) #Note this is assigned to size instead of shape
