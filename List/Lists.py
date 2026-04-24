#Lists are used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values.

# orderd, not chnage the order and new item is added t end of the liost
#changable- we can add, cha ge, modiefy pr remove the value from the list

thislist = ["apple", "banana", "cherry","apple"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# list length - len()

print(len(thislist))



# list item - can contain any data type and defferent datatypes in ssme list

list1=["apple", "banana", "mango"]
list2= [1,2,3,4,5]
list3= [True, False, False, True ]

list4=["sankalp", 1, 20, True, 10.1]

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(thislist[1])
"""

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
