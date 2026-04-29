# __init__() method

#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
#The __init__() method is used to assign values to object properties, 
# or to perform operations that are necessary when the object is being created.

#Note: The __init__() method is called automatically every time the class is being used to create a new object.

#Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age

p1 = Person("sankalp",20)

print(p1.name)
print(p1.age)
    

#Why Use __init__()?

#Without the __init__() method, you would need to set properties manually for each object:

#Create a class without __init__():

class Person1:
    pass

p1= Person1()
p1.name="sankalp"
p1.age=22

print(p1.name)
print(p1.age)

#With __init__(), you can set initial values when creating the object:


#DEFAULT VALUES IN __init__()

#You can also set default values for parameters in the __init__() method:

class Default:
    def __init__(self, name, age= 18):
        self.name= name
        self.age=age

p1=Default("sankalp")
p2=Default("gourav")
p3= Default("ashu",17)

print(p1.name, p1.age)
print(p2.name , p2.age)
print(p3.name, p3.age)

#multiple parameters

#we camn have multiple para,etrs in __init__() method

class mulPram:
    def __init__(self, name, model, year,color):
        self.name=name
        self.model=model
        self.year=year
        self.color=color

car= mulPram("bmw","s3",2026, "black")

print(car.name)
print(car.model)
print(car.color)
print(car.year)
        
