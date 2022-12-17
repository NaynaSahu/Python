#Write a program to prints the squares of all integers from 1 to 10  using while loop.
i = 1
while(i<10):
    print(i*i)
    i = i+ 1
#write a program to print count down from 10 to 1 using while loop.
i = 10 
while(i> 0):
    print(i)
    i = i-1
#Take a number from user and write a program for table of that number using while loop
i = int(input("enter the number = "))
a = 1 
while(a>10):
    print(i , "X" , a , "=" , i*a)

    a = a+1


#Write a program for printing odd numbers less than n(from user) using while loop.

i = int(input("enter the range "))
a = 1
while (a < i):
    if a % 2 != 0:
        print (a)
        
    a = a + 1
#write a puthon program to check the password and print the messahe that "Your password in correct" otherwise "Ypur password is wrong"
a = "123456@nayna sahu"
passw = input("enter your password = ")
i = 0
while(i in range(len(a))):
    if(passw[i] == a[i]):
        i = i+1
        if( i == len(a)-1 ):
            if(passw[i] == a[i]):
                print("Your password is correct")
 
    else:
        print("Your password is incorrect")
        break


    
    

