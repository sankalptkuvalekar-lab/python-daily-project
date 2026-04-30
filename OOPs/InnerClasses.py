#An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
#inner classes are useful for grouping classes that are only used in one place, making your code more organized.

class Outer:
    def __init__(self):
        self.name="outer"

    class Inner:
        def __init__(self):
            self.name="inner"

        def display():
            print("this is innner class")

outer=Outer()

print(outer.name)


#Accessing Inner Class from the Outside
#To access the inner class, create an object of the outer class, and then create an object of the inner class:


class Outer:
    def __init__(self):
        self.name="outer"

    class Inner:
        def __init__(self):
            self.name="inner"

        def display(self):
            print("this is innner class")

outer=Outer()
inner= Outer.Inner()
inner.display()
print(inner.name)
print(outer.name)


#Accessing Outer Class from Inner Class

#Inner classes in Python do not automatically have access to the outer class instance.
#If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()

inner = outer.Inner(outer)
inner.display()


#multiple inner classes

class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()