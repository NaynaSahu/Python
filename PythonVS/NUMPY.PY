from timeit import timeit
import numpy as np

# Difference between numpy array and python list 
# syntax to create array
x = np.array([1,2,3,4,5])
print(x) # will print the array
print(type(x)) # will print the type of array
print(x.ndim) # will give the dimension of array

# syntax to create list
y = [1,2,3,3,4,5]
print(y) # will print the list
print(type(y)) # will print the type in which the y is stored

# Cnverting a list to np array
y = [1,2,3,4,5]
x = np.array(y)

# taking the user input for the in the form of list and  converting it to np array
l = []
for i in range(1,9):
    a = int(input("enter the value :"))
    l.append(a)

print(l)
k = np.array(l)
print(k)

# multiple dimension array

x = np.array([[1,2,3,4],[1,2,3,4]]) # 2d array
print(x.ndim)

y = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]]) # 3d array
print(y.ndim)

z = np.array([1,2,3,4] ,ndmin= 10 ) # ndmin is for providing no. of dimension

# array filled with zeros and ones
# will directly form array no need of np.array 
a = np.zeros(4) 
print(a)

a = np.zeros([2,4]) # rows x columns 
print(a)

b = np.ones(5)
print(b)

b =np.ones([2,4]) # rows x columns
print(b)

# create an empty array 
a = np.empty(4) # 1d array

# create a array having some range 
b = np.arange(4) # output will be [0,1,2,3]

# create a diagonal ones 
x = np.eye(3)
print(x)

# linspace (the array is formed with same gape or space between the numbers)
l = np.linspace(0,10 , num = 5 )
print(l)

# create nupy array with randim numbers
#1
x = np.random.rand(4) #<- 4 is the size of array and will generate random 4 values from (0 to 1)
X = np.random.rand(2,5)  #<- 2X5 is the size of array and will generate random 4 values from (0 to 1)

#2
y = np.random.randn(5) # will give random numbers close to 0 and can ne -ve or +ve

#3
x = np.random.randf(4) # will give random numbers in float between 0 and 1 where 0 is included and 1 is excluded

#4
y = np.random.randint(1,5,4) # will provide random numbers in given range

# different data types of array 

w= np.array([1,2,3,4])# integer
x = np.array([1.2,1.3,1.4])# float
y = np.array(['a','b'])
z = np.array(["A",1,2])
k = np.array(x , dtype = np.int16)# 1 conversion of data type
k = np.array(x , dtype = "i")# 2 conversion of data type
k = np.float128(x) # 3 conversion of data type (using as a function)
k = y.astype(float)# 4 conversion of data type 

print(w.dtype)
print(x.dtype)
print(y.dtype)
print(k)

# ARTHMETIC OPERATION IN NUMPY ARRAY

a = np.array([1,2,3,4,5])
print(a+1)
print(a-1)
print(a%1)
print(a**1)
print(a*1)

print(np.min(a))
print(np.max(a))
print(np.argmax(a))# will provide the position or the index num of max value
print(np.argmin(a))# will provide the position or the index num of min value


a1 = np.array([1,2,3,4,5])
a2 = np.array([1,2,3,4,5])
print(a1+a2)

print(np.add(a1,a2))
print(np.subtract(a1,a2))
print(np.multiply(a1,a2))
print(np.divide(a1,a2))
print(np.reciprocal(a1))
print(np.mod(a1,a2))
print(np.abs(a1))# non negative values

a11 = np.array([[1,2,3,4],[1,2,3,4]])
a12 = np.array([[1,2,3,4],[1,2,3,4]])
# axis = 1 -> row , axis = 0 -> column 
print(np.min(a11,axis = 0))
print(np.max(a11,axis = 0))
print(np.min(a11,axis = 1))
print(np.sqrt(a11))
print(np.sin(a11))
print(np.cos(a11))
print(np.cumsum())
# same as above (addition , subtraction ....)

# SHAPE AND RESHAPING NUMPY ARRAY
a = np.array([1,2,3,4] , ndmin= 4)
print(a.shape)

b = np.array([1,2,3,4,5,6,7,8])# no. of elements should be equal to multiplication of the rows and columns
print(b.reshape(4,2))
print(b.reshape(2,2,2))
print(b.reshape(-1)) # for converting to 1D array

# BROADCASTING ERROR -> when we perform any arthmatic operation on array of numpy the dimension and the no.
# of elements should be same or should be according to matrices rule


# Iterating function

a = np.array([1,2,3,4] , ndmin= 4)
for i in np.nditer(a):
    print(i)

# changing data type while itrating
a = np.array([1,2,3,4] , ndmin= 4)
for i in np.nditer(a , flags =['buffered'] , op_dtypes=['S']):
    print(i)


