import numpy as np


# my_list=[1,2,3,4]
# my_array1=np.array(my_list)
# print(my_array1)
#
# my_list2=[11,44,66,33]
# my_lists=[my_list,my_list2]
# my_array2=np.array(my_lists)
# print(my_array2)
#
# list=[1,3,4,5]
# array1=np.array(list)
# print(array1)
#
# list2=[11,22,44,33]
# lists=[list,list2]
# array2=np.array(lists)#multidimensional array**
# print(array2)
# print(my_array2.shape)
# print(my_array2.dtype)
# print(np.zeros(5).dtype)
# print(np.ones([4,4]))
# print(np.empty(5))
# print(np.eye(4))
# print(np.arange(5))
# print(np.arange(5,34))
# print(np.arange(5,34,2))

# using arrays and scalars
# arr=np.array([[1,4,6,4],[1,6,3,4]])
# print(arr)
# print(arr*arr)
# print(arr-arr)
# print(1/arr)
# print(arr**3)

# # indexing arrays
# index=np.arange(0,10)
# print(index)
# print(index[5])
# slice_of_arr=index[0:6]
# print(slice_of_arr)
# print(slice_of_arr[:]=100)



#indexing in 2d arrays

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
# print(arr_2d)
# print(arr_2d[1])
# print(arr_2d[0])
# print(arr_2d[1,0])
# print(arr_2d[:1,:2])

# c=np.array([1,])
# print(c)
# print(arr_2d[2])
# print(arr_2d[0])
# arr2d = np.zeros((10,10))
# print(arr2d)
# arr_length=arr2d.shape[1]
# print(arr_length)
# for i in range(arr_length):
#     arr2d[i]=1
#     print(arr2d)

# for i in range(arr_length):
#     arr2d[i]=1
#     print(arr2d)


# arr2d=np.zeros((10,10))
# arrlength=arr2d.shape[1]
# print(arrlength)
# for i in range(arrlength):
#     arr2d[i]=i
#     print(arr2d)
# print(arr2d[[1,3,5,6]])


# array transposition
# arr=np.arange(50).reshape((10,5))
# print(arr)
# print(arr.T)

# arr3d=np.arange(40).reshape(4,5,2)
# print(arr3d)

# arrswap=np.array([[1,3,5]])
# print(arrswap.swapaxes(0,1))
# print(arrswap)



# Universal Array Function
# arr=np.arange(11)
# print(arr)
#
# # square root
# print(np.sqrt(arr))
# # exponential
# b=np.exp(arr)
# print(b)
# # random
# a=np.random.rand(10)
# print(a)
# c=np.random.rand(10)
# print(c)
# # Binary Functions
# print(np.add(a,c))
#Finding max or min between two arrays
# np.maximum(a,c)

# website = "http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
# import webbrowser
# print(webbrowser.open(website))





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# points = np.arange(-5,5,0.01)

# dx,dy=np.meshgrid(points,points)
# print(dx)
#
# z = (np.sin(dx) + np.sin(dy))
# print(z)
#
# print(plt.imshow(z))
# a=123
# print(type(a))
#
# error=50
# while error>1:
#     error=error/5
#     print(error)


import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2S
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)