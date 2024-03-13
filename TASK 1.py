"""
TASK 1 
Create a Python program that declares and initializes variables of different data types:
integer, float, string, and boolean. Print the values and types of these variables
"""
#declaration of variables and its datatypes
int_var = 65
flt_var = 0.76
str_var = "My book"
bool_var = 7 > 8

#Print values and variable types
print(int_var)
print(type(int_var))
print(flt_var)
print(type(flt_var))
print(str_var)
print(type(str_var))
print(bool_var)
print(type(bool_var))


"""
TASK 2(b)
Create a function that takes a string as input and returns True if it is a palindrome
reads the same backward as forward, False otherwise. 
"""

# Takes string as input

def is_Palindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        else:
            return True
 
# main function
a = "level"
ans = is_Palindrome(a)
 
if (ans):
    print("True, the string is a palindrome")
else:
    print("False the string is not a palindrome")