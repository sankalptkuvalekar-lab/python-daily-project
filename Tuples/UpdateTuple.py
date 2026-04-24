#CHANGE VALUE
#we cannot chnage the tuple elements but wr can do that by  converting the tuble into list and again list back to tuple
# tuple to list -  listname= list(tuplename)
 #list to tuple -   tuplename= tuple(listname)

myTuple=("sanku", "gouru", "ashu");
myList= list(myTuple); #this is list

myList[1]= ("baye")

myTuple= tuple(myList); #list conerted into tuble
print(myTuple)


#ADD ITEM
# #- saMe thing cant direct add so convert into list first

addTuple= (1,2,3,4,5)

addList = list(addTuple)
addList.append(7)

addTuple=tuple(addList)
print(addTuple)

#Add tuple to a tuple

tuple1= (1,2,3,4,5)
tuple2=(6,7,8,9)

tuple1+=tuple2

print(tuple1)


#REMOVE ITEM
#first convert to list , remove, convert back to tuple

removeTuple=("a","b","c","d","e")

removeList= list(removeTuple)

removeList.pop(2)  #removeList.remove("c")

removeTuple=tuple(removeList)
print(removeTuple)

#to delete complete tuple. - del

deleteTuple=(1,2,3,4,5,6,7)
del deleteTuple
print(deleteTuple) #it will shot the error