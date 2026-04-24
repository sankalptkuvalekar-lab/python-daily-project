#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

list1=["sankalp", "ashu", "gouru", "trupti", "tulasidas"]
list2=[]

for x in list1:
    if "a" in x:
        list2.append(x)


print(list2)        



listNum= [1,2,4,5,6,7]
listNum1=[]

for x in listNum:
    if x <5 :
        listNum1.append(x)

print(listNum1)



#wit₹h comorehensive just in 1 line

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)



#syntax
#newlist = [expression for item in iterable if condition == True]

#Condition
newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in fruits]

#iterable
newlist=[x for x in range(10)]
print(newlist)

newList = [x for x in range(10) if x>5]
print(newList)


#expression

#set all values to hello

fruits= ["apple", "banana", "chikoo", "strawberry"]

newList= ["hello" for x in fruits]

print(newList)

#convert all into uppercase letter

newList1= [x.upper() for x in fruits]
print(newList1)

#returns orang e insted opf banana

newList2= [x if x!= "banana" else "oragne" for x in fruits ]

print(newList2)