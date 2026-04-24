# true or false

print(10 > 9)
print(10 == 9)
print(10 < 9)

a=2020
b=222

if a>b:
    print("a is greater than b")

else:
    print("a is not greater than b")
    

#Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))


x = ""
y = 0

print(bool(x))
print(bool(y))



#function can return true

def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")

  """  Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

Example
Check if an object is an integer or not:
"""
x = 200
print(isinstance(x, int))
