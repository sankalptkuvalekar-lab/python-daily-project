#The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with
#  the same name that can be executed on many objects or classes.

#Function Polymorphism

#An example of a Python function that can be used on different objects is the len() function.

#For strings len() returns the number of characters:
string ="hello sankalp"
print(len(string))

#for tuple len() return the number f items
tup=("sankalpo", True, 0, False)
print(len(tup))


#for dictionary len() return number of key/value pairs

dict={
    "NAME": "SANKALP",
    "age": 23,
    "isMarried" :False
}
print(len(dict))




#Class Polymorphism

#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model=model
    
    def move(self):
        print("drive")

class Baot:
    def __init__(self, brand, model):
        self.brand= brand
        self.model=model
    
    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand= brand
        self.model=model
    
    def move(self):
        print("Fly")


c1 = Car("bmw","s20")
b1=Baot("vikramaditya", 2017)
p1=Plane("indid=go", 2000)


c1.move()
b1.move()
p1.move()

for x in (c1,b1,p1):
    print(x.brand, x.model)
    x.move()




#Inheritance Class Polymorphism

"""
What about classes with child classes with the same name? Can we use polymorphism there?

Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
"""
class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("sail")
    
class Plane(Vehicle):
    def move(self):
        print("fly")

c1=Car("bmw",2020)
b1=Baot("ins",2010)
p1=Plane("akasa",2023)

c1.move()
b1.move()
p1.move()

for x in (c1,b1,p1):
    print(x.model, x.brand)
    x.move()

"""
hild classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes."""