from array import array
from itertools import product
import numpy as np 
#Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.
arr = [1,2,3,4,4]
print(arr)
print("maximum indices = " , np.argmax(arr))
print("minimum indices = ", np.argmin(arr))
#Write a NumPy program to to create a 1-D array of 20 element spaced evenly on a log scale between 2. and 5.
arr = np.logspace(2.0 , 5.0 , 20)
print(arr)

#Write a NumPy program to sum and compute the product of a NumPy array elements.
a = np.array([1,2,3,4,5,6])
sum = np.sum(a)
product1 = np.prod(a)
print("sum is = ", sum)
print("product is = ", product1)
#Hint:np.sum() and np.prod()
#Write a NumPy program to calculate 50th, 40th and 90th percentiles for a sequence or single-dimensional NumPy array
arr = np.array([1,2,3,4,5,6,7,8] )

print(np.percentile(arr , 50 ))
print(np.percentile(arr , 40))
print(np.percentile(arr , 90))

# Write a NumPy program to add, subtract, multiply, divide arguments element-wise.

print("sum = " , np.add(2,5))
print("subtract = " , np.subtract(5,10))
print("multiply = " , np.multiply(4,7))
print("divide = " , np.divide(2,10))

# Write a NumPy program to get the powers of an array values element-wise.
arr = np.array(np.arange(8))
print(np.power(arr,6))

#Write a NumPy program to get the element-wise remainder of an array of division by 5.
arr = np.array([1,2,3,4,5,6])
print(np.remainder(arr,5))
#Hint:np.remainder(x, 5)
#Write a NumPy program to calculate the absolute value element-wise
arr =np.array([1,2,3,-5,-70,-34])
print(np.absolute(arr))
#Write a NumPy program to round elements of the array to the nearest integer. 
arr = np.array([1.56,1.67,5.78,6.90])
print(np.round(arr , decimals=1))
#Write a Python program to find the maximum and minimum value of a given flattened array. 
arr = np.array([1,2,3,4,5,6,7,8,9,1])
print(np.max(arr))
print(np.min(arr))
#Write a NumPy program to get the minimum and maximum value of a given array along the second axis.
arr = np.array([[1,2,3,4,5,6],[7,8,9,1,2,3]])
print(np.max(arr , axis=1))
print(np.min(arr , axis=1))
#Write a NumPy program to compute the median of flattened given array
arr = np.array([2,3,4,5,6,7,8])
print(np.median(arr))
#Write a NumPy program to compute the mean, standard deviation, and variance of a given array along the second axis.
arr = np.array([[1,2,3,4] , [5,6,7,8] ])
print(np.mean(arr , axis=1))
print(np.std(arr , axis=1))
print(np.var(arr , axis=1))


#Write a NumPy program to compute the covariance matrix of two given arrays
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
print(np.cov(x,y))
#Write a NumPy program to compute cross-correlation of two given arrays. 
x = np,array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
print(np.corrcoef(x,y))
#Write a NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis.
arr = np.array([[1,2,3,4] , [1,2,3,4]])
a = np.max(arr , axis=1)
b = np.min(arr , axis=1)
print(np.subtract(a,b))

# Create a vector of size 10 with values ranging from 0 to 1, both excluded 
arr = np.array(np.arange())
