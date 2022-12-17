
#Take values of length and breadth of a rectangle from user and check if it is square or not.
from ast import If
from calendar import month


length = int(input("enter the length = "))
breadth = int(input("enter the breadth = "))
if(length == breadth):
    print("it is a square")
else:
    print("it is not a square")

#Program to check whether a person is eligible to vote or not.

age = int(input("enter your age = "))
if(age >= 18):
    print("you are eligible to vote")
else:
    print("you are not")

"""A school has following rules for grading system:

a. Below 25 - F

b. 25 to 45 - E

c. 45 to 50 - D

d. 50 to 60 - C

e. 60 to 80 - B

f. Above 80 - A

Ask user to enter marks and print the corresponding grade. """

a = float(input("enter your marks = "))
if (a < 25 ):
    print("grade is F")
elif(24<= a < 45):
    print("grade is E")
elif(45 <= a < 50):
    print("grade is D")
elif(50 <= a < 60):
    print("grade is C")
elif(60 <= a <80 ):
    print("grade is B")
elif(a>80):
    print("grade is A")



#Take input of age of 3 people by user and determine oldest and youngest among them.
a = int(input("enter the age 1 "))
b = int(input("enter the age 2 "))
c = int(input("enter the age 3 "))
if(a>b & a>c):
    print("a is oldest")
    if(b>c):
        print("b is middle child")
        print("c is smallest")
    elif(c>b):
        print("c is middle chile")
        print("b is smallest")
    
if(b>a & b>c):
    print("b is oldest")
    if(a>c):
        print("a is middle child")
        print("c is smallest")
    elif(c>a):
        print("c is middle chile")
        print("a is smallest")
    
if(c>a & c>b):
    print("c is the oldest")
    if(a>b):
        print("a is middle child")
        print("b is smallest")
    elif(b>a):
        print("b is middle chile")
        print("a is smallest")
    

#Write a program to print absolute vlaue of a number entered by user.

a = float(input("enter the number "))
print(abs(a))

'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

Number of classes held

Number of classes attended.

And print

percentage of class attended

Is student is allowed to sit in exam or not.'''

classes = int(input("enter the number of classes held = "))
classes1 = int(input("enter the number of classes attended "))
a =  (classes1*100)//classes
if(a>=75):
    print("you are allowed to give exam")
else:
    print("not allowed")
#Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
medical = input("do you have a medical cause? type Y/N ")
classes = int(input("enter the number of classes held = "))
classes1 = int(input("enter the number of classes attended "))
a =  (classes1*100)//classes
b = "Y"
if(a>=75  or b.casefold() == medical ):
    print("you are allowed to give exam")
else:
    print("not allowed")
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.Ask user for their salary and year of service and print the net bonus amount.

year = int(input("enter the years of service = "))
salary = int(input("enter your salary = "))
a = (5*salary)//100
if(year>5):
    print("the increased salary is = ", salary + a)
else:
    print("no bonus")

#Write a Python program to convert month name to a number of days.
month = input("enter the month = ")
if(month.casefold() == "january"):
    print("31")

elif(month.casefold() == "february"):
    print("28")

elif(month.casefold() == "march"):
    print("31")
elif(month.casefold() == "april"):
    print("30")
elif(month.casefold() == "may"):
    print("31")
elif(month.casefold() == "june"):
    print("30")
elif(month.casefold() == "july"):
    print("31")
elif(month.casefold() == "august"):
    print("31")
elif(month.casefold() == "september"):
    print("30")
elif(month.casefold() == "october"):
    print("31")
elif(month.casefold() == "november"):
    print("30")
elif(month.casefold() == "december"):
    print("31")


#Write a Python program that reads two integers representing a month and day and prints the season for that month
a = int(input("enter the no. of month = "))
b = int(input("enter the no. of day = "))
if(a == 12 or a<=2 and 0<b<=31 ):
    print("season is winter")
elif(3<=a>=5 and 0<b<=31):
    print("season is summer")
elif(6<=a>= 9 and 0<b<=31 ):
    print("season is monsoon")
elif(10<=a>=11 & 0<b<=31 ):
    print("season is post monsoon")



