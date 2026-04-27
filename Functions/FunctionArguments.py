#Information can be passed into functions as arguments.
#@Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

#A function with one argument:

def name_func(name):
    print("my name is", name)

name_func("sankalp")
name_func("gourav")
name_func("ashu")
name_func(11)
name_func(False)


#Parameters vs Arguments

#The terms parameter and argument can be used for the same thing: information that are passed into a function.

#A parameter is the variable listed inside the parentheses in the function definition
#An argument is the actual value that is sent to the function when it is called.

def my_func(email):    #email is parameter
    print("hellow", email)
 
my_func("sankalp@gmai.com")   # "sankalp@gmai.com" is arguments



#multiple argumenst

def multiple_arg(fname, lname):
    print("my full name is:", fname , lname)


multiple_arg("sankalp", "kuvalekar")

#multiple_arg("sankalp") #this will thrigh the error beacuse no. of arguments should same as number of parameters


#DEFAULT PARAMETER VALUES
#You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def default_function(name="sankalp"):
    print("I AM", name)


default_function()
default_function("gourav")
default_function("ashwini")


#Keyword Arguments
#You can send arguments with the key = value syntax.

def key_arguments(animal,name):
    print("i have a", animal)
    print(f"my {animal} name is {name}")

key_arguments(animal="dog", name="rocky")   #dog stored in animal.  rocky stpored in name

#if u assign key opposite


key_arguments(name="dog", animal="rocky")   #rockeystored in animal.  rockydog


#positional arguments
#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:
 
def key_arguments(animal,name):
    print("i have a", animal)
    print(f"my {animal} name is {name}")

key_arguments("cat", "billu")

key_arguments("billu","cat") # position change values will changer

#Mixing Positional and Keyword Arguments
#However, positional arguments must come before keyword arguments:

def mix_arguments(animal, name , age):
    print(f"i have a {animal} named {name} and {name} is {age} year old")

mix_arguments("billu", name="cat", age=5)



#PASSING DEFFERENT DATA TYPE

#list datatyoe

def list_function(fruits):
    for x in fruits:
        print(x)

my_fruits=["apple","banana", "mango"]
list_function(my_fruits)

#dictionary

def dict_function(details): 
        print("name:", details["name"])
        print("age:",details["age"])
    
my_details={"name":"sankalp", "age":24}

dict_function(my_details)


#Return Values

def sum_function(x,y):
    return x+y

print(sum_function(10,20))


#Returning Different Data Types

def listReturn_fun():
    return["apple","banana","mango"]

fruits= listReturn_fun()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#tuple

def tupleReturn_func():
    return ("bat","ball")

x,y=tupleReturn_func()
print(x)
print(y)

#Positional-Only Arguments
 #   ,/  use after the argument- this specify that u are using only posoition arguents it will not allow the keywprd argumnts

def positionOnly_fun(name,/):
    print("hellow", name)

positionOnly_fun("sankalp")

"""
the below copde will throgh the error
def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")
"""




#Keyword-Only Arguments

# *,  use befpre the argumens - which means you ahev to manditorily use thw key for the argumenst

def keywordOnly_fun(*, name,):
    print(name)

keywordOnly_fun(name="sankalp")

"""
    this will thrugh an error
    def keywordOnly_fun(*, name,):
    print(name)

keywordOnly_fun("sankalp")
"""

#Combining Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d, e,):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)