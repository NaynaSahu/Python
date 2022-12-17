# Accept a list of 5 float numbers as an input from the user and print their sum.
from re import I


a = input("enter a value = ")
b = a.split()
k=0.0
print("the list is = ",b)
for x in range(len(b)):
    b[x] = float(b[x])
    k = k + b[x]
print(k)

# Write a program print the addition, subtraction, multiplication and division of given numbers.

a = float(input("enter 1st num = "))

b = float(input("enter 2nd num = "))
print("for addition type ADD")

print("for subtraction type SUB")
print("for multiplication type MUL")
print("for dividion type DIV")
c = input("enter operation = ")
if( c == "ADD"):
    print(a+b)
elif( c == "SUB"):
    print(a-b)
elif(c == "MUL"):
    print(a*b)
elif(c == "DIV"):
    print(a/b)

# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

a = input("enter a value = ")
b = a.split()
k=0.0
print("the list is = ",b)
for x in range(len(b)):
    b[x] = float(b[x])
    k = k + b[x]
    print(x , "+" , b[x] ,"=",k )

#Write a program to accept a string from the user and display characters that are present at an even index number.

a = input("enter a statement = ")

print ("your string is = ",a)
for x in range(len(a)):
    if(x % 2 == 0):
        print(a[x])

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
a = [1,2,3,45,4]
if a[0] == a[len(a)-1]:
    print("True")
else:
    print("False")

# Write a program to iterate the given list of numbers and print only those numbers, which are divisible by 5.
a = [5,10,20,25,3,5,67,10]
for i in range(len(a)):
    if(a[i] % 5 == 0):
        print(a[i])



    



