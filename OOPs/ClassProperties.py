#Properties are variables that belong to a class. They store data for each object created from the class.

#Create a class with properties:
class Person:
    def __init__(self, name , age):
        self.name=name
        self.age=age
    
p1=Person("sankalp", 22)

print(p1.name)
print(p1.age)

#Access Properties
#u can access the properties using . (dot)notation

print(p1.name)

name= p1.name
print(name)

#Modify Properties
#Change the age property:
print("old age:", p1.age)
p1.age=24

print("new age:", p1.age)

#Delete Properties
#u can delete using del keyword

#delete age
print("before deelete", p1.age)
p1.age
try:
 pass
finally:
   print("after delete: age del;eted")



#Class Properties vs Object Properties

#Properties defined inside __init__() belong to each object (instance properties).
#Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

#Class property vs instance property:

class Person:
   category = "human" #class property
   def __init__(self, name, age):
      self.name=name  #instance/object property
      self.age=age    #instance/object property

p1=Person("sankalp", 11)
p2=Person("ashu",10)

print(p1.category, p1.name, p1.age)
print(p2.category, p2.name,p2.age)



#Modifying Class Properties
#When you modify a class property, it affects all objects:

Person.category="animal"

print(p1.category, p1.name, p1.age)
print(p2.category, p2.name,p2.age)


#Add New Properties

p3=Person("sankalp", 11)
p3.hobby="vricket"
p3.favfood="chicken"

print(p3.name)
print(p3.age)
print(p3.hobby)
print(p3.favfood)

#Note: Adding properties this way only adds them to that specific object, not to all objects of the class.


      

