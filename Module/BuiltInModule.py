#tere are some built in modules present in the putghon u can use those whenever you want thenm

import platform

x=platform.system()
print(x)

#he dir() function can be used on all modules, also the ones you create yourself.
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
y=dir(platform)
print(y)