"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

#CREATE A CLASS  - use class keywprd

#Create a class named MyClass, with a property named x:

class MyClass:
    x=10


#creating the object - Now we can use the class named MyClass to create objects:
#Create an object named p1, and print the value of x:

p1= MyClass()
print(p1.x)


#Multiple Objects - we can create multiople objects using same clas

p1=MyClass()
p2=MyClass()
p3=MyClass()

print(p1.x)
print(p2.x)
print(p3.x) 

#here  Each object is independent and has its own copy of the class properties.


#Delete Objects
#You can delete objects by using the del keyword: 

del p3



#The pass Statement
#class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.

class MyClass1:
    pass