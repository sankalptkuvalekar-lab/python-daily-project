#the else statement is executed when the if condition (and any elif conditions) evaluate to False.

a=30
b=20

if a>b:
    print("a is greatrer")
else:
    print('b is greater')


#if, elif, and else

tempreture=23

if tempreture>30:
    print("its hot")
elif tempreture>20:
    print("its warm")
elif tempreture>10:
    print("its cool")
else:
    print("its cold")

    #odd, even num

num=10
if num % 2 == 0:
    print("even")
else:
    print("odd")


username = "email"

if len(username)>0:
    print(f"welcome, {username}!")
    print("welocme, ",username,"!")
else:
    print("error: username cannot be emopty")

