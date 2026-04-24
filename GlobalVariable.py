x="Awesome"

def func():
  print("Python is "+ x)
  
  func();




y= "good"

def myFunc():
  y="fantastic"
  print("python is "+y)

myFunc();
print("python is "+y)



#The global Keyword
#to create gloval variable inside the funvtion use global keyword

z= "nice"

def myFunc1():
  global z
  z = "very very good"
  print("pythin is "+z)

myFunc1()

print(z)