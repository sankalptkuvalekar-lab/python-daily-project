#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression

#syntax: lambda arguments : expression


x = lambda a : a+5
print(x(5))

#Lambda functions can take any number of arguments:

x = lambda a,b,c,d : a+b*c+d

print(x(1,2,3,4))

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

doubler=myfunc(2)
tripler=myfunc(3)

print(doubler(11))
print(tripler(12))

#Lambda with Built-in Functions

#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().


#1 The map() function applies a function to every item in an iterable:

numbers=[1,2,3,4,5]
doubled = list(map(lambda x: x*2,numbers))
print(doubled)


#2 The filter() function creates a list of items for which a function returns True:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#The sorted() function can use a lambda as a key for custom sorting:

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)