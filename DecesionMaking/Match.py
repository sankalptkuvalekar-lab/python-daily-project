#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.

#syntax
"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

day = 4

match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")




#Default Value _ (uderscore) -if you want a code block to execute when there are not other matches

day = 4

match day:
     case 6:
        print("saturday")
     case 7:
         print("sunday")
     case _:
        print("no weekend")



#Combine Values
#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 3

match day:
    case 1 | 2| 3| 4| 5:
        print("weekdays")
    case 6|7:
        print("wow weekend")
    case _ :
        print("day dpesnt exist")



#If Statements as Guards 
#u can add if statements in the case evaluation as an extra condition-check:
month = 5
day = 4

match day:
    case 1 | 2| 3| 4| 5 if month == 4: 
        print("weekdays in april") 
    case 6|7:
        print("wow weekend in april")
    case 1 | 2| 3| 4| 5 if month == 5 :
        print("weekdays in may")
    case 6|7:
        print("wow weekend in may")
    
