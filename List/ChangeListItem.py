thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values

thislist = [1,2,3,4,5]
thislist[2:4]= [8,9]
print(thislist)


thislist= [10,20,30,40,50]
thislist[3:6] = [15,25,35]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

lists=[1,2,3,4,5,6]
lists.insert(1,10)
print(lists)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])  #banana

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist)