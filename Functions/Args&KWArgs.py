#*args and **kwargs allow functions to accept a unknown number of arguments.

#What is *args?
#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments:

def arg_function(*args):
    print("Type:", type(args))
    print("first elememnt:", args[0])
    print("second element:", args[1])
    print("all arge:", args)

arg_function("apple","banana")    


def arg_func(*kids):
    print(kids[2])

arg_func("sanku","gouru","ashu","sanmu",1,2)


#Using *args with Regular Arguments

#You can combine regular parameters with *args.
# Regular parameters must come before *args:

def regArg_fun(greeting, *names):
     for x in names:
         print(greeting,x)



regArg_fun("SANKALP", "ASHU", "gouru", "mamu","kaamu", 1,2)



#A function that calculates the sum of any number of values:

def sum_func(*numbers):
    total = 0
    for num in numbers:
        total+=num
    return total

print(sum_func(12,34))
print(sum_func(12,34,56,78))
print(sum_func(1,2,3,4,5,6,3,3,3,3,3,3,34,4,5,5,67,7))



#find the max num

def maxNum_func(*numbers):
    if len(numbers)==0:
        return None
    max_num=0
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num

print(maxNum_func(1,2,3,4,5,6,7,8,9887,665,43,3))



#What is **kwargs?
#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter nam
#This way, the function will receive a dictionary of arguments and can access the items accordingly:


def kwargd_fun(**name):
    print("his last name is",name["lname"])


kwargd_fun(fname="sankalp" ,lname="kuvalekar")


def mydetails_funct(**mydetails):
    print("type:", type(mydetails))
    print("name", mydetails["name"])
    print("age:", mydetails["age"])
    print("city:", mydetails["area"])
    print("add data:", mydetails)

mydetails_funct(name="sankalp", age=24, area="karwar" )



#Combining *args and **kwargs
"""
The order must be:

regular parameters
*args
**kwargs"""


def combine_function(title, *args, **kwargs):
    print("Title:", title)
    print("positiional arguments:" , args)
    print("keyword arguments:" , kwargs)

combine_function("user info", "sankalp", "ashu" ,age=20, city="karwar")



#Unpacking Arguments

#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

#Unpacking Lists with *

def sum_func(a,b,c):
    return a+b+c

numbers=(1,2,3)
result = sum_func(*numbers)  #Same as: my_function(1, 2, 3)
print(result)


#Unpacking Dictionaries with **

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")