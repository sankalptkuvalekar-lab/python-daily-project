#If you have only one statement to execute, you can put it on the same line as the if statement.
a=10
b=20

if a>b: print("a is greater than b")



# short if el;se
a= 20
b=30

#Also known as TURNERY OPERSTOR

print("A") if a>b else print("B")



#You can also use a one-line if/else to choose a value and assign it to a variable:

a= 10
b=20

bigger = a if a>b else b
print("bigger is:", bigger)#syntax: variable = value_if_true if condition else value_if_false



#Multiple Conditions on One Line

a=10
b=10

print("A") if a> b else print("=") if a==b else print("B")



username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
