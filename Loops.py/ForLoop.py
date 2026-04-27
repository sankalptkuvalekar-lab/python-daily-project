#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#The for loop does not require an indexing variable to set beforehand.

list1= ["apple", "banana", "mango", "orange"]

for x in list1:
    print(x)


#Looping throug string

string1 = "SANKALP"

for x in string1:
    print(x)

#The break Statement
list1= ["apple", "banana", "mango", "orange","strwaberry"]

for x in list1:
    print(x)
    if(x=="mango"):
        break


string2= " ASHWINI"

for x in string2:
    if(x=="N"):
        break
    print(x)


#The continue Statement

tuple1=("sonu","gouru", "sanku", "Ashu")

for x in tuple1:
    if(x=="sanku"):
       continue
    print(x)

#The range() Function
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):   #value of 0 to 5
  print(x)
  


#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
print("#########")
for x in range(2,7):
    print(x)


#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#so the syntX IS
# range (staring_value(optional by default 0), ending_value, increment_value(by default 1))

#Else in For Loop

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
 
for x in range(6):
     print(x)
else:
    print("completed")


#Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(10):
    print(x)
    if x == 5:
        break
else:
    print("continue")


   
 #The pass Statement
 #for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass
