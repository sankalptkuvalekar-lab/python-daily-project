#AND

a= 10
b=20
c=30

if a<b and a<c:
    print("a is smaller")

#OR

if a<b or a>c:
    print("anything okay")


#not 
if not a>b:
    print("ulta")


username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")


  score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")


  username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")