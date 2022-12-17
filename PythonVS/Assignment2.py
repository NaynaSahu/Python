#Write a Python program to create a set

Fruits = {"apple", "mango", "banana" , "orange" , "papaya","watermelon" , "melon"}
print(Fruits)
for x in Fruits:
    print(x)

#If the item to remove does not exist, remove() will raise an error.

Alphabets = {'a','b','c','d'}
i =Alphabets.remove('e')

#Return a set that contains the items that only exist in set y, and not in set x:

x = {1,2,3,4,5,6}
y = {6,7,8,9,0,0}
print(x.difference(y))

#Compare 3 sets, and return a set with items that is present in all 3 sets:

x = {1,2,3,4,5,6}
y = {6,7,8,9,0,0}
z = {1,2,3,54,5,6}
w = x.intersection(y,z)
print(w)

#What if no items are present in both sets?
#Return False if one ore more items are present in both sets:Try it yourself

A = {"ANISHA", "NAYNA" , "SHRIYANSHI"}
B = {"RABBIT","ANT","NAYNA"}
Z = A.isdisjoint(B)
print(Z)

#Write a Python program to add member(s) in a set

A = {"ANISHA", "NAYNA" , "SHRIYANSHI"}
A.update([1,2,3,4])
print(A)

#Write a Python program to remove an item from a set if it is present in the set
B = {1,2,3,4,5}
B.remove(2)
print(B)

#Write a Python program to check if a given value is present in a set or not.

A = {"apple" , "bannana" , "mango"}
print("apple" in A)

#Write a Python program to check if two given sets have no elements in common. 

A = {"ANISHA", "NAYNA" , "SHRIYANSHI"}
B = {"RABBIT","ANT"}
Z = A.isdisjoint(B)
print(Z)

#Write a Python program to find maximum and the minimum value in a set.
#hint: Use max(set) and min(Set)

setA = {1,2,3,4,50}
print(max(setA))
print(min(setA))

#Write a Python program to check if a given set is subset of itself and subset of another given set
#Hint: Use <

setC = {1,2,3,4,5,6,7,8,9}
setD = {1,2,3,4,5}
print(setC>setD)

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