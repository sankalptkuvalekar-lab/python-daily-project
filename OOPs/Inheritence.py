#Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#CREATING A PARENT CLASS
#Any class can be a parent class, so the syntax is the same as creating any other class:

#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def print_name(self):
        print(self.fname, self.lname)

p1=Person("sankalp", "kuvalekar")
p1.print_name()


#Create a Child Class

#To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class:     syntax- class child_class(parent_class):

class Student(Person):
    pass

#Now the Student class has the same properties and methods as the Person class.

s1=Student("ashwini", "shetkar")
s1.print_name()




#Add the __init__() Function

#So far we have created a child class that inherits the properties and methods from its parent.
#We want to add the __init__() function to the child class (instead of the pass keyword).

#Note: The __init__() function is called automatically every time the class is being used to create a new object.
#class Student(Person):
#  def __init__(self, fname, lname):


#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() functio
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
       Person.__init__(self,fname, lname)
   

s1=Student("ashu","bashu")

s1.print_name()

#Now we have successfully added the __init__() function, 
# and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

#Use the super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

s1=Student("ashu","bashu")

s1.print_name()

#By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.


#Add Properties
#Add a property called graduationyear to the Student class:



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)


class Person:
   def __init__(self, fname, lname):
      self.fname=fname
      self.lname=lname
    
   def printname(self):
      print(self.fname, self.lname)



class Student(Person):
   def __init__(self, fname, lname, passyear):
      super().__init__( fname, lname)
      self.passyear=passyear

s1=Student("sankalp","kuvalekar",2019)


print(s1.passyear)


#Add Methods

#Add a method called welcome to the Student class:
class Person:
   def __init__(self, fname, lname):
      self.fname=fname
      self.lname=lname
    
   def fullName(self):
        print(self.fname, self.lname)     



class Student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.year=year
    
   def welcome(self):
      print(f"hi {self.fname} {self.lname}, your graduatio year is {self.year}")

s1=Student("gouru", "tk", 2025)

s1.welcome()
s1.fullName()




#If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden.