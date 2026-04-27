#Generators are functions that can pause and resume their execution.
#When a generator function is called, it returns a generator object, which is an iterator
#codeinside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

  #Instead of using return, generators use the yield keyword.


  #The yield Keyword
  #The yield keyword is what makes a function a generator.
  #When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

  #Generators Saves Memory
 # Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))


#Using next() with Generators#You can manually iterate through a generator using the next() function:

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#When there are no more values to yield, the generator raises a StopIteration exception:
'''
def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) # This will raise StopIteration
'''

#close() Method
#
# The close() method stops the generator:#

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

#send() Method
#The send() method allows you to send a value to the generator:#


def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")



#Generator Expressions
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))