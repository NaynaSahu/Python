#Write a python program with for loop to iterate over a list using range()
l =[1,2,3,4,5,6,7,8,9]

for i in range(len(l)):
    print(l[i])

#Write a Python Program to print Cubes of all numbers present in a list

l = [23,4,5,6,7,7,88,9]

for i in range(len(l)):
    print("the cube of ",l[i]," is ",l[i]**3 )
#Generates a list of 5 values starting from 1 ***")
l = list()

for i in range(5):
    l.append(i)
print(l)
    
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(7):
    if(i==3 or i == 6):
        continue
    print(i)

#Write a Python Program to print the Product of first 10 natural numbers
j = 1
for i in range(1,11):
    j = i*j

print ("product of the natural numbers are = ", j)
#Write a Python program to display all the elements before number 71 in the list [11, 9, 77, 10, 90, 3, 19]
list = [11, 9, 77, 10, 90, 3, 19]

for i in range(len(list)):
    if(list[i] == 77):
        break
    print(list[i])

#Accept number from user and calculate the sum of all number between 1 and given number

a = int(input("enter the range = "))
b = 0
for i in range(2,a):
    b = a+b
print("your sum is = ", b)


#Print multiplication table of given number(from user)
a = int(input("enter the number = "))

for i in range(1,11):
    print(a," X ",i," = ",a*i)
# Given a list iterate it and display numbers which are divisible by 5
l =[35,57,35,24,2445,50,10,13,24]

for i in range (len(l)):
    if(l[i]%5 == 0):
        print(l[i])
#Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
l = [23,45,56,6,7,8,50,55,35,80, 140,165,150,155, 140]
for i in range(len(l)):
    if(l[i]%5 == 0 ):
        if(l[i] >= 150):
            break
        print(l[i])