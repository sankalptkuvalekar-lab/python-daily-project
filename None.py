#None is a special constant in Python that represents the absence of a value
#Its data type is NoneType, and None is the only instance of a NoneType object.

#Variables can be assigned None to indicate "no value" or "not set"

x= None
print(x)

print(type(x))

#Comparing to None
#use is or not is fopr compzring NONE

result = None
if result is None:
    print("no resulkt yet")
else:
    print("result is reasy")

    #using not is

result = None
if result is not None:
        print("you can seee the result")
else:
        print("waiting for the reuslt")

#True or False Nnone is always False

print(bool(None))


#Functions returning None
#A function without a return statement returns None:

def myFunvction():
      x=10
    
x=myFunvction()
print(x)

