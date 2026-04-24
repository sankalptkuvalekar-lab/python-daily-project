#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")


#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "mango", "grapes")

(red, yellow, green) = fruits

print(red)
print(yellow)
print(green)



#Using Asterisk *

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)
