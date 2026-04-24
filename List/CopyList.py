#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

#we have 3 defferent wways to copy 

# 1 use copy()

mylist = [1,2,3,4,5]
copylist = mylist.copy()
print(copylist)

copylist.append(10)
print(copylist)
print(mylist)



#2 Use the list() method

mylist1= [1,2,3,4,4,6,7,8,9,0]

mylist2= list(mylist1)

print(mylist2)


#3 Use the slice Operator :

mylist10= [0,9,8,7,6,5,4,3,2,1]
copyMylist = mylist10[:]
print(copyMylist)
