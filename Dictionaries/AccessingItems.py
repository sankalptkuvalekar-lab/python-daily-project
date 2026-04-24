# accessing value using perticular key

dict1={
    "name": "sankalp",
    "age" : 23,
    "isMarried": False
}
x= dict1["isMarried"]
print(x)

#using get() method

y=dict1.get("age")
print(y)


#Get Keys
#The keys() method will return a list of all the keys in the dictionary.

print(dict1.keys())


#key will get update after adding the new value


dict1={
    "name": "sankalp",
    "age" : 23,
    "isMarried": False
}

x= dict1.keys()
print(x)

dict1["villlage"] = "harwada"
print(x)

#Get Values
#The values() method will return a list of all the values in the dictionary.

x= dict1.values()
print(x)

#values will get update after adding the new value

dict1["home"]="sweet"


print(x)

dict1["home"]="not sweet"


print(x)


#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.

x=dict1.items()
print(x)


dict1["home"]="tulasi"
print(x)
dict1["phno"]=12345
print(x)


#check if key exist
ct1={
    "name": "sankalp",
    "age" : 23,
    "isMarried": False
}
if "name" in ct1:
    print("yes")
else:
    print("no")
