#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

#When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

a=30
b=30

if a>b:
    print("a is greate")
elif a<b:
    print("b is greater")
elif a== b:
    print("a and b are equal")




#Multiple Elif Statements

day = "monday"

if day == "sunday":
    print("sunday")
elif day == "monday":
    print("monday")
elif day == "tiesday":
    print("tuesday")
elif day == "wednesday":
    print("wednesday")
elif day == "thursday":
    print("thursday")
elif day == "friday":
    print("friday")  


age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
 
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
