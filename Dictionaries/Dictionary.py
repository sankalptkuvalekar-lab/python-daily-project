#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#ctionary items are ordered, changeable, and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


newdict ={
    1: "sankalp",
    2: "goirav",
    3: "ashu"
}
print(newdict)

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:

duplicatedict= {
    "name":"sankalp",
    "age":36,
    "Lname": "sankalp",
    "name":"gourav"
    

}
print(duplicatedict)


#length - len()

print(len(duplicatedict))

# any data type allowed
typeDict= {
    "name":"sankalp",
    "age":12,
    1:"good",
    "married":False,
    "hobbies": ["cricket","books","song"]
}
print(typeDict)

#to knowtype

print(type(typeDict))

#he dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway", num =2)
print(thisdict)