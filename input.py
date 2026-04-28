

"""
#Python allows for user input.

print("enter your name:")
name= input()
print(f"hellow {name}")

#Using prompt - input on same lne

name = input("enter user name:")
print("welcome",name)

#Multiple Inputs
#You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:

name = input("enter your name")
print("welcome", name)

fruit=input('ypur favorite fruit:')
animal=input("enter your fav animal:")
food= input("enter your fav food:")

print(f"{name}, your fav fruit is {fruit}, and u like {animal}, and your fav food is {food}")

"""
#Input Number
#The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

#You can convert the input into a number with the float() function:
import math
x= input("enter a number:")

y=math.sqrt(float(x))

print(f"the sqrt of {x} is {y}")

#Validate Input

#Keep asking until you get a number:
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")