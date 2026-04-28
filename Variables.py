a= 10
b = 20
name= 'sankalp' 
age= 25
height= 2.5
married = False
string = "sanllap123"

print(a,b)
print("name:",name )


x = 4       # x is of type int
x = "sanku" # x is now of type str
print(x)


#if you want tio specify the data tyipe

t = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(t)
print(z)

#get() - to get the type of the variavle

x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = 'John'


#case sensiutive

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

CarName="Volvo"
print(CarName)



#Multiple variable

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

fruits= ["apple", "banana", "mango", 1]
a, b, c, d= fruits
print(a)
print(b)
print(c)
print(d)


#output variable

x= "python"
y= "is very good"
z= "language"

print(x,y,z)
print(x+" "+y+" "+z)


x="sankalp" 
y= 10
z= True

print(x,y,z)
