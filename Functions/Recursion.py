#Recursion is when a function calls itself.
#This has the benefit of meaning that you can loop through data to reach a result.

#A simple recursive function that counts down from 5:

def countdown(n):
    if n<=0:
        print ("done")
    else:
        print(n)
        countdown(n-1)

countdown(10)


#Base Case and Recursive Case

#Every recursive function must have two parts:
#A base case - A condition that stops the recursion
#A recursive case - The function calling itself with a modified argument
#Without a base case, the function would call itself forever, causing a stack overflow error.

def factorial(n):
    #base case
    if n==0 or n==1:
        return 1
    #recursive class
    else:
        return n * factorial(n-1)


print(factorial(10))


#Fibonacci Sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))



#Recursion Depth Limit
import sys
print(sys.getrecursionlimit())


#If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())