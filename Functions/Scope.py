#A variable is only available from inside the region it is created. This is called scope.

#Local Scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300 
  print(x)

myfunc()


#Function Inside Function
#As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

#The local variable can be accessed from a function within the function:

def myfun():
  x=456
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfun()


#GLOBAL SCOPE
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.

x=123

def myfnction():
  print(x)

myfnction()

print (x)


#Naming Variables
#If you operate with the same variable name inside and outside of a function, Python will treat them as
#two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

y=20

def yfuncton():
  y=30
  print(y)

yfuncton()

print(y)


#Global Keyword# use global keywprd it will makw the variable goable

x=20

def globalKey():
  global x
  x=50
  print(x)

globalKey()
print(x)


#Nonlocal Keyword

#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.

def nonlocat():
  x="john"
  def nonlocalword():
    nonlocal x
    x="sankalp"
  nonlocalword()
  return x

print(nonlocat())



"""
The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace

"""
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

