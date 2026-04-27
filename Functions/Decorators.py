#Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function.

#Define the decorator first, then apply it with @decorator_name above the function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "hello world"

print(myfunction())

"""

The function changecase is the decorator.

The function myfunction is the function that gets decorated.
"""


#Multiple Decorator Calls

def changable(func):
    def myiiner():
        return func().upper()
    return myiiner

@changable
def myfunction1():
    return "hekllow india"

@changable
def myfunction2():
    return "welcome to india"

print(myfunction1())
print(myfunction2())

#Arguments in the Decorated Function


def chnagable1(func):
    def innerFunction(x):
        return func(x).upper()
    return innerFunction

@chnagable1
def muFunction(name):
    return "hello," + name

print(muFunction("sankalp"))


#*args and **kwargs

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))




#Decorator With Arguments

def changedcase(n):
    def changedcase(func):
        def innerFunction():
            if n==1:
                a= func().upper()
            else:
                a= func().lower()
            return a
        return innerFunction
    return changedcase


@changedcase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())



"""
Multiple Decorators
You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.
"""

def changable1(func):
    def myinner():
        return  func().upper()
    return myinner

def changable2(func):
    def myinner():
        return "hellw " + func() + " welcome"
    return myinner
    
@changable1
@changable2
def myFunction():
    return "sankalp"

print(myFunction())

#Preserving Function Metadata

#unctions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

#Normally, a function's name can be returned with the __name__ attribute:
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#But, when a function is decorated, the metadata of the original function is lost.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)


#Import functools.wraps to preserve the original function name and docstring.

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)