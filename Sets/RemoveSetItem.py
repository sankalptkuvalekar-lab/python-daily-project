# 1 remove(). - if the element doesnt in set throgh the error

set1 = {"apple," "banana", "mango", "grapes", "chickoo"}
set1.remove("chickoo")
#set1.remove("chickoo")   #this will throgh an error
print(set1)


# 2 discard(). - if the element doesnt in set it will not throgh the error

set1 = {"apple," "banana", "mango", "grapes", "chickoo"}
set1.discard("chickoo")

print(set1)

set1.discard("chickoo")   #this will not throgh an error
print(set1)


#3 pop()     removes. the random itsm

set1 = {"apple," "banana", "mango", "grapes", "chickoo"}
set1.pop()
print(set1)


#4 clear().  empty the set



set1.clear()
print(set1)


# 5 delete the set completel;y   del

set1 = {"apple," "banana", "mango", "grapes", "chickoo"}
del set1
print(set1) #error



