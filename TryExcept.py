"""

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""
#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement:

#The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("an exceptionoccured")
a=10
b=20
print(a+b)


#ince the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error:

#Many Exceptions
#Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("x is not definer")
except:
    print("something else wentn wrong")

    #else
#You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
    print("hello")
except:
    print("error occur")
else:
    print("nithung wrong ")



    #finally -The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
 print(x)
except:
  print("An error occured")
finally:
   print("Execution completed")


    #Raise an exception
#To throw (or raise) an exception, use the raise keyword.

x=-1

if x<0:
    raise Exception("only positive numbers are allowed")

#You can define what kind of error to raise, and the text to print to the user.

y=" "
if not type(y) is int:
    raise TypeError("only integeres are alowed")


