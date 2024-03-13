"""Write a Python program that asks the user to enter their age.
 If the age is greater than or equal to 18, 
print "You are an adult." Otherwise, print "You are a minor."""

#Variable age intitialized to take input of age
Age = float(input("Please enter your age:"))

#conditional statements for printing output

if Age <= 18:
        print("You are a minor ")
else:
        print("You are an adult")
