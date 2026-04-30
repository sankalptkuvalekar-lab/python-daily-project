#To delete a file, you must import the OS module, and run its os.remove() function:

#Remove the file "mynewfile.txt":

import os
#os.remove("/Users/sankalp/mynewfile.tx")

#Check if File exist:
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


  #Delete Folder
  #Delete Folder

import os
os.rmdir("/Users/sankalp/Desktop/linkedinLearning")

#Note: You can only remove empty folders.

