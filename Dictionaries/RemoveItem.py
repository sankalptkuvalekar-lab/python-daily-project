# 1 pop() - remove item with specifirs key name

dict1= {
    "name": "sankalp",
    "age": 24,
    "ismearried" : False,
    "city": "Karwar"
}

dict1.pop("age")
print(dict1)


#2 popitem() removes te last inserted item


dict1= {
    "name": "sankalp",
    "age": 24,
    "ismearried" : False,
    "city": "Karwar"
}
dict1.popitem()
print(dict1)

#del() removes the utem from the specified key name

dict1= {
    "name": "sankalp",
    "age": 24,
    "ismearried" : False,
    "city": "Karwar"
}

del dict1["name"]
print(dict1)


# del ketword will also remove the whole dictionary

del dict1
#print(dict1) #NameError: name 'dict1' is not defined. Did you mean: 'dict'?




#3. clear().  clears all item from the dictionary

dict1= {
    "name": "sankalp",
    "age": 24,
    "ismearried" : False,
    "city": "Karwar"
}

dict1.clear()
print(dict1)