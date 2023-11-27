'''
Author: Deeplaxmi Lambture
Course: 100days of Python (Code with Harry)

'''

#pip is a package manager to install python modules.
print("Hello World \"good morning\" and have a nice day",7,'\n', 12*7)

print("Hey", 25,11,sep="~", end="009\n")


### ~ Variables and Data Types
a = 1
b = "Deep"
print(a,b)

'''
Numeric data: int, float, complex
int = 1
float = 2.2
complex= 3 +  4j


Text data: str
str = "Hello World", "Python Programming"

Boolean data: True / False

Sequenced Data: list, tuple
lists = [1, "Deeo", [1,2],["Deep","Laxmi"]] = mutation

tuple: immutable = (1, (1,2))

Mapped data: dict
dict1 = {"name":"Deeplaxmi","age": "20"}

in python, everything is an object

'''

#to check type of variable you can use type(var)


'''
Typecasting: conversion of one data type into another
Explicit conversion: conversion performed by a developer manually as per requirement
Implicit conversion: 

'''
a ="1"
b = "2"
print(a+b) #it will concat the string and return 12

print(int(a)+int(b)) #explicit type casting

c= 1.9
d = 8
print(c+d) #implicit type casting



'''
Strings sequence or array of textual data.
Strings are used when working with Unicode characters
'''

name = "I will write up a sentence and I can print each character in this sentence either manually (by accessing index name[0]) or using a for loop. For now, let's print with for loop"
for character in name:
    print(character)

#string slicing = square brackets are used in slicing

stringname= "Deeplaxmi"  #print 'laxmi' and print it's length
#name[0:4] : includes 0 but not 4

print("\n",stringname[4:9], len(stringname[4:9]), stringname[:10], stringname[:], stringname[:-3], stringname[-1:-6], "\t", stringname[-3:-1])

nm="Harry"
print(nm[-4:-2])

'''
String functions:

'''

String1 = "name! !!"
print(String1.lower())
print(String1.upper())
print(String1.capitalize())
print(len(String1))
print(String1.rstrip("!")) #only strips the right part of string
print(String1.replace("name","Deep"))
print(String1.split(" "))
print(String1.center(50))
print(String1.count("e"))
print(String1.endswith("!"))
print(String1.endswith("m",1,3))
print(String1.find("m"))
print(String1.index("m")) #raises exception if not found
print(String1.isalnum())
print(String1.isprintable())
print(String1.isspace())
print(String1.istitle())
print(String1.startswith("n"))
print(String1.swapcase())
print(String1.title())



'''
if, if-else, if-else elif, nested statements
'''

age = int(input("Enter your age: "))
if(age<18):
    print("you are an underage person")
elif(age<=30):
    if(age < 20 ):
        print("You should focus on your bachelors")
    elif(age < 25 ):
        print("stop juggling between your passions and your career")
    else:
        print("you should focus on your career")
else:
    print("you are an full-grown adult")







