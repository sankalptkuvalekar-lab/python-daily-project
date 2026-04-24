#Set items are unordered, unchangeable, and do not allow duplicate values.
 #Set items are unchangeable, but you can remove items and add new items.

thisset= {"apple", "banana", "mango", "grapes"}
print(thisset)


#duplictre not allowed 

set1={1,2,3,9,8,4,5,1}
print(set1)       #output - {1, 2, 3, 4, 5} 

#True and 1 are considered as same and treated as duplicate and false wiuth 0

set2= {1,2,3,4,5,0,9,True, False}
print(set2)


# lenfth of set - len()

set1={1,2,3,4,5,6}
print(len(set1))

#suppoerts all datatypes and ,ixed

set1={1,2,3,4}
set2={"apple", "banana", "mango"}
set3={True,False}
mixdSet={1,2,"apple", True,False}

#to know set datatype type()

print(type(set1))

#The set() Constructor

set1= set(("apple",1,True))

