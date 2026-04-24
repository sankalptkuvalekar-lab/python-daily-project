#Append Items
#add item tio the end of the list append()

lists = ["sankalp", "gourav", "ashu", "sonu"]
lists.append("surya")
print(lists)

#Insert Items
#to inserrt an item to a specific index. - insert(inde_no, value)

lists.insert(0,"shreyash")
print(lists)

#Extend List
# to append(add) elements from another list to curent list -  extend()      current_list.extend(another_list)

list1= [10,20,30,40,50]
list2= [60,70,80,90,100]
list1.extend(list2)
print(list1)


#Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
