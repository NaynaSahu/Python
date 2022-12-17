#Write a name from user and print a greeting message using user defined function
from ast import Str


fname = input("enter your name = ")
def setFirstName():
    print("Hi" ,  fname , "Welcome to NMIMS")

setFirstName()
#Take a number from user and define a function to find its abesolute value.
num = int(input("enter the number : "))
def FindAbdoluteValue():
    print(abs(num))

FindAbdoluteValue()
#Define a function to check whether x is even or odd 
num = int(input("enter the number : "))
def FindTheNumber():
    if(num % 2 == 0):
        print("the number is even ")
    else:
        print("the number is odd")

FindTheNumber()
# Define a function to Test if two words start with the same character, and returns True/False. Case distinction is ignored.
def Check_Words():
    a = "nayna"
    b = "nitya"
    if (a[0]==b[0]) :
        print("true")
    else:
        print("false")

Check_Words()
# Define a function to covert the temperature from degree celsius to degrees Fahrenheit


def Convert(v):
   print(v,"C")
   b = (v * 9/5)+ 32
   print(b,"F")

Convert()

#Define a Python function to multiply all the numbers in a list. 
def list_Multilier(l=list()):
     a = 1
     for i in range(len(l)):
        a = a* l[i]

     print(a)
     

list_Multilier([1,2,3,4,4,5])

#Define a Python function to check whether a number is perfect or not.

def perfect_Number( a = int ):
    b = 0
    for i in range(1,a):
        if(a % i == 0):
            b = b+i

        
    if (b == a):
        print("It is a perfect Number")
    else:
        print("It is not a perfect Number")

perfect_Number(56)



#Write a Python function to create and print a list where the values are square of numbers between 1 and 20 (both included).

def square_List():
     l = list()
     for i in range(1,21):
        a = i * i
        l.append(a)

     print(l)

square_List()



#Write a Python function to find the Max of three numbers.
def maximum_Number():
    a = int(input("Enter 1st num"))
    b = int (input("Enter 2nd num"))
    c = int(input("Enter 3rd num"))
    if(a>=b & a>=c):
        print("1st is greater")

    elif(b>=a & b>=c ):
        print("2nd is greater ")
    else:
        print("3rd is greater")
maximum_Number()


#Create a function that can accept two arguments name and age and print its value
from tokenize import String


def intro(name = String , age = int ):
    print("My name is ", name , ". My age is ", age)

intro("Nayna Sahu" , 19)

#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
def calculation(a , b ):
    c = input("add / sub")
    if (c == "add"):
        print("ans is ", a+b)

    elif(c == "sub"):
        print("ans is ", a-b)

calculation(34,56)
# Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
def showEmployee(EmpName = String , salary = 9000):
    print(EmpName , salary)

showEmployee("Nayna")



#Assign a different name to function and call it through the new name


def mistake():
    print("its a mistake")

mistake1()