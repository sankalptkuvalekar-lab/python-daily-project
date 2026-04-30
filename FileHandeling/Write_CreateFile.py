#Write to an Existing File
#To write to an existing file, you must add a parameter to the open() function:

"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

#aoopend "a"

with open("/Users/sankalp/myfile.txt", "a") as f:
    f.write(" the file has been added with this line by using append 'a'" )

    #open and read the file after the appending:
with open("/Users/sankalp/myfile.txt") as f:
    print(f.read())

#Overwrite Existing Content

#To overwrite the existing content to the file, use the w parameter:

#Note: the "w" method will overwrite the entire file.

with open("/Users/sankalp/myfile.txt", "w") as f:
    f.write("oh the 'w' mrhod is overwrite all my content to this line")

with open("/Users/sankalp/myfile.txt") as f:
    print(f.read())

#Create a new file

"""
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists

"""


f= open("/Users/sankalp/myfile.txt", "x")

#Note: If the file already exists, an error will be raised.
