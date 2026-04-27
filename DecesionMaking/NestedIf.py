age = 23

if age>10:
    print('age is above 10')
    if age>20:
        print("age ois above 20")
        if age>30:
            print('age is above 30')
else:
    print("ae is les then 10")



    #Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.

    #multiple conditions

age=22
has_license=False

if age>=18:
        if has_license:
            print("you can drive")
        else:
            print("ypu should have licenmse to drive")
else:
        print("you sre too small not eligible")


score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


username = "Emil"
password = ""
is_active = True

if username:
    if password:
        if is_active:
            print("Login successfull")
        else:
            print("account activation required")
    else:
        print("password not matchimh")
else:
    print("username is incorrect")