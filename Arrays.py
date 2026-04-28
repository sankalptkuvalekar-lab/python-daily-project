#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

#o work with arrays in Python you will have to import a library, like the NumPy library.

#Arrays are used to store multiple values in one single variable:



#An array is a special variable, which can hold more than one value at a time.

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW" #imstead of thisa


#this is array
cars=["bmw", "ferrari", "benz"]
print(cars)

#accessing the item from array
print(cars[0])

#modifying the value
cars[0] ="tayota"

print(cars)

#toknow the length pf the array len()

print(len(cars))


#Looping Array Elements

for i in cars:
    print(i)

#adding  new element to existing array.  .append()
cars.append("mahindra")

for i in cars:
    print(i)


#Removing Array Elements. pop(index)   , remove("value")

cars.pop(2) 
print(cars)


cars.remove("tayota")
print(cars)


"""

array methods 

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""