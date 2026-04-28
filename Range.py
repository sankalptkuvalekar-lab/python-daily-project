#The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

#This set of numbers has its own data type called range


#Creating ranges

#The range() function can be called with 1, 2, or 3 arguments,
#range(start, stop, step)

"""
Call range() With One Argument
If the range function is called with only one argument, the argument represents the stop value.


The start argument is optional, and if not provided, it defaults to 0.

range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).
"""

x = range(3, 10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))


x = range(3, 10, 2)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))


x = range (10,100,10)
print(list(x))


#Ranges are often used in for loops to iterate over a sequence of numbers.

for i in range(10):
    print(i)

#Using List to Display Ranges

print(list(range(5)))
print(list(range(10,20)))
print(list(range(10,20,3)))

#Slicing Ranges
r = range(10)
print(r[2])
print(list(r[:3]))



#Membership Testing
#Ranges support membership testing with the in operator.
r = range(0,10,2)
print(list(r))
print(6 in r)
print(7 in r)


#Length
#Ranges support the len() function to get the number of elements in the range.

r = range(0,10,2)
print(len(r))