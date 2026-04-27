# using for

dict1= {
    "name": "sankalp",
    "age": 24,
    "ismearried" : False,
    "city": "Karwar"
}




#printing all keys one by one

for x in dict1:
    print(x)

#or use .keys
for x in dict1.keys():
      print(x)


  
  
    #printing all values oneby one
for x in dict1:
        print(dict1[x])


#or use .values()
for x in dict1.values():
      print(x)


#loop using .items()

for x, y in dict1.items():
  print(x,":", y)