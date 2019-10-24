print ("\033c")
print ("++++++++++    welcome to PyMath!    ++++++++++\n")
print ("    Select your question : \n")
print ("        1 - Is this number prime ?")
print ("        2 - Comming soon ...\n")
number = input("        :")

if number == 1 :
    execfile('prime-number.py')
elif number == 2 :
    print("this is not released !")
elif number == "Q" :
    exit
else :
    print("Invalid choice!")
    exit