"""
here are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.


"""


#1 union(). u can use |

set1= {1,2,3,4,5}
set2= {"a", "b", "c", "d"}

set3=set1.union(set2)
print(set3)
#or
set3=set1 | set2
print(set3)

#multiple sets
set1= {1,2,3,4,5}
set2= {"a", "b", "c", "d"}
set3 = {True,False}
set4= {"a",1,True}

finalSet=set1.union(set2,set3,set4)
print(finalSet)
#or
finalSet= set1 | set2 | set3 | set4
print(finalSet)

#can join deffetent iterls with set
set1= {1,2,3,4,5}
tuple1= (10,20,30,40)

final=set1.union(tuple1)
print(final)



#Update - update(). hanges originalmset bdoesnt return nrew set

set1= {1,2,3,4,5}
set2= {"a", "b", "c", "d"}

set1.update(set2)
print(set1)


#intersaction() or  & - onlyb returns the common values which are same in both

set1 ={1,2,3,4,5}
set2= {1,7,3,9,0,7,9}

set3=set1.intersection(set2)
print(set3)
#or

set3= set1 & set2
print(set3)


#intesaction_update = do same thing but it will chan ge the orignal set instead of returning new swer

set1.intersection_update(set2)

print(set1)

# true and 1 consider as same and 0 and false consioder as same 
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)


#Difference.   defference() or - - returns the uncommon elememts [present in first set

set1 ={1,2,3,4,5}
set2= {1,7,3,9,0,7,9}

set3=set1.difference(set2)
print(set3)

#or

set3= set1- set2
print(set3)

#defference_update() - same thung but not return new set change the original set


set1 ={1,2,3,4,5}
set2= {1,7,3,9,0,7,9}

set1.difference_update(set2)
print(set1)


#Symmetric Differences -symmetric_difference()  or ^the elements not commo in both the set

set1 ={1,2,3,4,5}
set2= {1,7,3,9,0,7,9}

set3=set1.symmetric_difference(set2)
print(set3)

#or

set3= set1 ^ set2
print(set3)


#symmetric_difference_update() :nonew set change thenoriginal set

set1 ={1,2,3,4,5}
set2= {1,7,3,9,0,7,9}

set1.symmetric_difference_update(set2)
print(set1)


