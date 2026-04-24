"""
Operator	Description	                                                                         Example	
in 	        Returns True if a sequence with the specified value is present in the object	     x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	 x not in y
"""

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list



x = ["apple", "banana"]

print("mango" not in x)

# returns True because a sequence with the value "banana" is in the list


#memborship in string

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)