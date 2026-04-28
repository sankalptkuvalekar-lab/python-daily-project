#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

#RegEx Module
#built in opackage called re  ussed tp work with regular expressrion

import re

#Search the string to see if it starts with my and ends woth sankalp

txt = "my name is sankalp"
x=re.search("^my.*sankalp", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


  #RegEx Functions
  """
  
Function	Description
findall.    	Returns a list containing all matches
search	      Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
  
  """


#findall() - 

txt= "my name is sankalp my fathdr name is tulasidas and my mother name sis trupti"
x=re.findall("my", txt)
print(x)

txt1="my name is sankalp"

x=re.findall("sanku", txt)
print(x)


#The search() Functioon
"""
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:"""

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


#If no matches are found, the value None is returned:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#The sub() Function
#The sub() function replaces the matches with the text of your choice:

txt= "my name is sankap"
x=re.sub("sankap", "gourav", txt)
print(x)

#You can control the number of replacements by specifying the count parameter:


txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)