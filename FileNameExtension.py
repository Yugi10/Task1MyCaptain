import os
filename = input ("Please enter the name of your file with extension :\n")
extn = os.path.splitext (filename)
print ("\nThe file name without extension is :\n" , extn[0])
print ("\nThe extension of file name " + str (filename) + " is :\n" , extn[1])
