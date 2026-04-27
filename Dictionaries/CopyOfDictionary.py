#1 using .copy()

typeDict= {
    "name":"sankalp",
    "age":12,
    1:"good",
    "married":False,
    "hobbies": ["cricket","books","song"]
}

newDict = typeDict.copy()
print(newDict)
print(typeDict)

# using. dict(). key word


typeDict= {
    "name":"sankalp",
    "age":12,
    1:"good",
    "married":False,
    "hobbies": ["cricket","books","song"]
}


newDict= dict(typeDict)

print(newDict)
print(typeDict)
