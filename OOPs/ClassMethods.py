#Methods are functions that belong to a class. They define the behavior of objects created from the class.

#Note: All methods must have self as the first parameter.

class Person:
    def __init__(self, name):
        self.name=name
   
    def greet(self):
        print("hello, ", self.name)

p1=Person("sankalp")
p2=Person("gourav")

p1.greet()
p2.greet()


#Methods with Parameters

#Methods can accept parameters just like regular functions:

class Calculator:
    def add(self, a, b):
        return a+b
    
    def mul(self, a , b):
        return a*b
    
cal1=Calculator()

print(cal1.add(10,20))
print(cal1.mul(10,2))


#Methods Accessing Properties

#Methods can access object properties using self:

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
   
    def greet(self):
        print(f"hellow {self.name} , you are {self.age} years old")

p1=Person("sankalp", 23)
p1.greet()


#Methods Modifying Properties
#Methods can modify the properties of an object using self:


class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def celeb_Birthday(self):
        self.age+=1
        print(f"happy birthday {self.name}, yor are now {self.age}")

per= Person("ashu", 22)
per.celeb_Birthday()



#The __str__() Method

#The __str__() method is a special method that controls what is returned when the object is printed:

#Without the __str__() method:
class Withoudstr:
    def __init__(self, name, age):
        self.name= name
        self.age=age

w1=Withoudstr("sankalp", 10)

print(w1)   # <__main__.Withoudstr object at 0x101898ad0>   - this will be the output not understandable

#With the __str__() method:

class Withoudstr:
    def __init__(self, name, age):
        self.name= name
        self.age=age
    
    def __str__(self):
        return f"name is {self.name} and age is {self.age}"

w1=Withoudstr("sankalp", 10)
print(w1)


#Multiple Methods
# a class can have multiple methids that work toghather
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()


#Delete Methods
#using del keyword
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

#p1.greet() # This will cause an error