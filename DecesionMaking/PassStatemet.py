#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

"""
when to use pass
When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement late
"""
a=10
b=20

if a>b:
    pass




#pass in development
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

  #pass vs Comments
#A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). You need pass where Python expects a statement, not just a comment.

score = 85

#if score > 90:
  # This is excellent
# This will raise an IndentationError


#While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.

def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet