myFamily ={

"child" : {
    "name":"sankalp",
     "age":25
},
"father" : {
    "name": "tulsidas",
    "age":60
},
"mother" : {
    "name": "trupti",
    "age":55

}

}
print(myFamily)


#or 

child = {
     "name":"sankalp",
     "age":25
}
Father = {
    "name": "tulsidas",
    "age":60
    }
Mother = {
    "name": "trupti",
    "age":55
}

myFam = {
    "child" : child,
    "Father": Father,
    "Mother": Mother

}
print(myFamily)

#Access Items in Nested Dictionaries

print(myFam["Father"]["name"])


#Loop Through Nested Dictionaries
#using items()
for x, obj in myFam.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])