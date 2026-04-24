lists= [1,2,3,4,5,6,7,8,9]
for x in lists:
     print(x)



     #Loop Through the Index Numbers
   #Use the range() and len() functions to create a suitable iterable.

for i in range(len(lists)):
    print(lists[i])
    

#Using a While Loop

list1= ["apple", "banana", "mango", "pineapple"]
i=0

while i < len(list1):
     print(list1[i])
     i=i+1


     #Looping Using List Comprehension
     thislist = ["apple", "banana", "cherry"]
     [print(x) for x in thislist]
     