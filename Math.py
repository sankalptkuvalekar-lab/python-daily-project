#Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

#Built-in Math Functions

x= min(10,20,40,3,45,90)
y= max(10,20,40,3,45,90)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:

z = abs(-89.7)
print(z)


#The pow(x, y) function returns the value of x to the power of y (x^y).

a=pow(5,4)  #5*5*5*5
print(a)


#The Math Module

#Python has also a built-in module called math, which extends the list of mathematical functions.

#To use it, you must import the math module:

import math

#The math.sqrt() method for example, returns the square root of a number:

x = math.sqrt(64)
print(x)


#The math.ceil() method rounds a number upwards to its nearest integer, and
#  the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

b=math.floor(10.3)
c=math.ceil(10.3)

print(b)
print(c)

#The math.pi constant, returns the value of PI (3.14...):

x=math.pi

print(x)