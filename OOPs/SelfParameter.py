#The self parameter is a reference to the current instance of the class.
#It is used to access properties and methods that belong to the class.


#Use self to access class properties:
class Person:
    def __init__(self, name, age):
         self.name=name
         self.age= age

    def greet(self):
         print("hello my name is:", self.name , "and i am", self.age, "years old" )
        
person1= Person("sankalp", 24)
person2= Person("ashu",22)

person1.greet()
person2.greet()

#Note: The self parameter must be the first parameter of any method in the class.

#Without self, Python would not know which object's properties you want to access:
#The self parameter links the method to the specific object:
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()


#self Does Not Have to Be Named "self"

#It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any method in the class:

#Use the words myobject and abc instead of self:

class Selfnames:
   def __init__(myobject, name, age):
          myobject.name= name
          myobject.age= age

   def greet(abc):
       print("hi im", abc.name , "and my age is:", abc.age)

p1=Selfnames("sankalp", 22)

p1.greet()

#While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
       

#Accessing Properties with self
#Access multiple properties using self

class Car:
    def __init__(self, name, color, year):
        self.name=name
        self.color=color
        self.year=year

    def greet(self):
        print(f"name:{self.name} and manufactured year {self.year}, color of car {self.color}")

c1=Car("tayota","red",2021)

c1.greet()


#Calling Methods with self
#Call one method from another method using self:

class MethodWithSelf:
    def __init__(self, name):
        self.name=name
    
    def greet(self):
        return "hello. "+  self.name

    def welcome(self):
        message= self.greet()
        print(message , "welcome")

m1=MethodWithSelf('SANKALP')

m1.welcome()
