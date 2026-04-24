#remove()

lists= [1,2,3,4,5]
lists.remove(1)
print(lists)


#If there are more than one item with the specified value, the remove() method removes the first occurrence:


lists =[1,2,3,4,2,3,4,1]
lists.remove(1)
print(lists)


#Remove Specified Index

#pop()

lists2= ["sankalp", "ashu", "gouru", "surya"]
lists2.pop(1)
print(lists2)

#If you do not specify the index, the pop() method removes the last item.

lists2.pop()
print(lists2)


#it can be also done by usint keywprd - del

thislist= ["sankalp", "ashu", "gouru", "surya"]
del thislist[0]
print(thislist)

#deletes entiure list
del thislist
#print(thislist)

#Clear the List

# clear(). - this will remove content but klist remains

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)