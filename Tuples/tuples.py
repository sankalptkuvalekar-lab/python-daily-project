#Tuple items are ordered, unchangeable, and allow duplicate values.
#order will not chnage ghave defined order
#we cannot change, add, remove items from tuples once cresated
#can have otems with same name

thistuple=("apple", "banana", "mango", "chikoo")
print(thistuple)

#Tuple Length - len()

size=len(thistuple)
print(size)

#Create Tuple With One Item

tuple1=("apple",)  #even single element should separated with tuhe coma
print(tuple1)

tuple2=("apple") #thius is noty an tuple this is wrpmg X 
print(tuple2)

# can be any datatype

tuples1=(1,2,3,4,5)
tuples2=("apple","banana", "mango")
tuples3=(True, False, False)
tuplesMixed=(1,"a", "apple", True)

#type() - datatype pf tup[le ios tuples

print(type(tuples1))


#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.

tupleconstructor = tuple((1,2,3,4,5))
print(tupleconstructor)