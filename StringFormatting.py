#F-Strings
#F-string allows you to format selected parts of a string.
#To specify a string as an f-string, simply put an f in front of the string literal, like this:

txt= f"my name is sankalp"
print(txt)


#Placeholders and Modifiers
#{} - {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

marks=10
txt=f"my marks are {marks}"
print(txt)

#A placeholder can also include a modifier to format the value.
#: followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 34
txt=f"the price is {price:.2f} rupees"
print(txt)

#You can also format a value directly without keeping it in a variable:
txt = f"the price is {90:.2f} rupees onlt"
print(txt)

#Perform Operations in F-Strings

txt=f"the multiplication rersult of 20 and 30 is {20*30}"
print(txt)

#You can perform math operations on variables:
a=10 
b=20

txt=f"the sum of a and b is {a+b} and the product of a and b is {a*b}"

print(txt)

#You can perform if...else statements inside the placeholders:

price=47
txt=f"the price is {'expesive' if price>50 else 'cheap' }"
print(txt)


#Execute Functions in F-Strings
#Use the string method upper()to convert a value into upper case letters

string= "apple"
txt=f"converted {string} into uppercase: {string.upper()}"
print(txt)

#u can use the custome functions

def muyFunction(x):
    return x * 10

txt=f"the 10th time of the number 10 is {muyFunction(10)}"
print(txt)


#More Modifiers
"""
Formatting Types
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

"""

#STRING FORMAT
"""
Before Python 3.6 we used the format() method to format strings.

The format() method can still be used, but f-strings are faster and the preferred way to format strings.

"""

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#index number
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))