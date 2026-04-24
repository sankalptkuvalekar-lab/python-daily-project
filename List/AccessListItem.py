thislist = ["apple", "banana", "cherry"]
print(thislist[1])

"""

Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item





thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third




#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")