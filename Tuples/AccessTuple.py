thistuple=("apple", "banana", "mango", "chikoo")
print(thistuple[1])

#negative index
thistuple=("apple", "banana", "mango", "chikoo")
print(thistuple[-1]) #-1 - chikoo, -2 - mango ... 


#Range of Indexes
print(thistuple[1:3])

print(thistuple[:3])

print(thistuple[2:])

#negative indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#Check if Item Exists - using in keywordz

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "apple" in thistuple:
    print("apple exists")
else:
    print("apple doesnt exist")
