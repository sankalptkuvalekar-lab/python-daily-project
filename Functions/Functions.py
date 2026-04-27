 #block of code which only runs when it is called.
#A function can return data as a result. A function helps avoiding code repetition.

#Creating a Function

#In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_funtion():
    print("welcome to my function")
    
#Calling function
my_funtion()

#we call call same function multiuple times
my_funtion()
my_funtion()
my_funtion()


#Function Names
"""
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)

ex:
calculate_sum()
_private_function()
myFunction2()"""

#TO AVOID THE SAMW THING WIOTING AGAIN AND AGAIN WE USE THE FUNCTION

num=10
print("square:", num*num)

num=20
print("square:", num*num)

num=30
print("square:", num*num)

#instead of this

def sqaure_function(num):
    return num*num

print(sqaure_function(10))
print(sqaure_function(20))
print(sqaure_function(30))

#Return Values
#Functions can send data back to the code that called them using the return statement.
#When a function reaches a return statement, it stops executing and sends the result back:

def return_function():
    return "hellow im returing the value"

message = return_function()
print(message)



def get_greeting():
  return "Hello from a function"

print(get_greeting())



#The pass Statement
#fUNCTION CANNOT BE EMPTY SO use can use pass to skip for tha moment it will not through any erpror

def my_function():
    pass