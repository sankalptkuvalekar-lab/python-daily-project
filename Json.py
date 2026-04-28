#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript object notation.

#JSON in Python



#Parse JSON - Convert from JSON to Python

#If you have a JSON string, you can parse it by using the json.loads() method.
#The result will be a Python dictionary.
import json

#some json:

x= '{"name": "sankalp", "age":16, "natinality": "india"}'

#parse x

y=json.loads(x)

## the result is a Python dictionary:
print(y["age"])


#Convert from Python to JSON
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None


#Convert Python objects into JSON strings, and print the values:
# """

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



"""
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
"""


#Convert a Python object containing all the legal data types:#

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


#Format the Result

#Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

print(json.dumps(x, indent=4))


#Use the separators parameter to change the default separator:
