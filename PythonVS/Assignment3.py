#Write a Python script to add a key to a dictionary.

A = {"first" : "anisha" , "sec" : "Nayna" , "third" : "Shriyanshi"}
A["fourth"] = "Ant"
print(A)

#Write a Python script to concatenate following dictionaries to create a new one

A = {1:23 , 2 : 34 , 3 : 45 }
B = {4: 67 , 5: 89 , 7: 90}
D = {"dict1" : A , "dict2" : B}

print(D)


#Write a Python script to check whether a given key already exists in a dictionary.

A = {"first" : "anisha" , "sec" : "Nayna" , "third" : "Shriyanshi"}
print ("first" in  A)

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are cube of keys.

d = dict()

for i in range(1,16):
    d[i] = i**3
print(d)

#Write a Python program to multiply all the items in a dictionary.
dict= { 1 : 45 , 2 : 67 , 3: 67 , 4: 80}
i = 1
for x in dict:
    i = i* dict[x]
print(i)

#Write a Python program to convert two lists into a dictionary

A = [1,2,3,4,5,6]
B = [10,20,30,40,50,60]
C = dict(zip(A,B))
print(C)