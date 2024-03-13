# %%
num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
squared_sum_num = num_1**2 + num_2**2
print('The sum of the squares for the given numbers is:', squared_sum_num)

# %%
Num_1 = int(input())
i = int(input())
Num_1 = Num_1**2 + i**2
print('Answer :', Num_1)

# %%
My_numbers = [20,13,32,17,55,12,1,43,4]
My_numbers.sort()
print(My_numbers)

# %%
My_girlfriends = ['Nessa', 'Amera', 'Harriet', 'Lizzy', 'Law', 'Nana', 'Constance', 'Mabel', 'Christy']
My_girlfriends.sort(reverse=True)
print(My_girlfriends)

# %%
# This function calculates the area of a right triangle
def compute__area(base, height):
    Area = 0.5 * (base) * height
    return Area

try:
    # Takes input for parallel sides of the trapezium and the height.
    base = float(input("Enter the length of the base: "))
    height = float(input("Enter the height of the right triangle: "))

    # Calculate the area
    Area = compute__area(base, height)

    # Display the result
    print(f"The area of the right triangle is: {Area:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numerical values for the base and height.") # error message provided user input invalid value


# %%
# Function to calculate the area of a trapezoid
def calculate_trapezoid_area(parallel_Side1, parallel_Side2, height):
    area = 0.5 * (parallel_Side1 + parallel_Side2) * height
    return area

# Input for base1, base2, and height
Parallel_Side1_str = input("Enter the length of the first base: ")
Parallel_Side2_str = input("Enter the length of the second base: ")
height_str = input("Enter the height of the trapezoid: ")

# Check if the input can be converted to float
if Parallel_Side1_str.isnumeric() and Parallel_Side2_str.isnumeric() and height_str.isnumeric():
    Parallel_Side1 = float(Parallel_Side1_str)
    Parallel_Side2 = float(Parallel_Side2_str)
    height = float(height_str)

    # Calculate the area
    area = calculate_trapezoid_area(Parallel_Side1, Parallel_Side2, height)

    # Display the result of the calculation if valid inputs are given or throw an error if invalid inputs are given
    print(f"The area of the trapezoid is: {area:.2f}")
else:
    print("Invalid Input! Please check and enter a valid base and height. ")

# %%
import random    #prints a random number from specified range
A = random.randrange(1,12)
print("Your random number is:" , A)

# %%
a = "I have started coding and it's quite refreshing" #prints length of a string
print(len(a))

# %%s
b = "My mum is a very wonderful woman" #slicing
S = b[1:5]
print(S)

# %%

print(b.isupper())

# %%
print(b.replace("wonderful","Nice"))

# %%
character_name = "Martin"
character_age = "50"
print("My name is " + character_name + ", and i'm " + character_age)

# %%
quantity = 3
itemo = 567
price = 49.7
myorder = "I want {} pieces of item {} for {} dollars" #literals
print(myorder.format(quantity, itemo, price))

# %%
a = 10
b = 3.322
c = 7j
d = int(b)
e = float(a)
f = complex(b)
g = complex(a)
print(type(a))
print(type(b))
print(type(c))
print(d)
print(e)
print(f)
print(g)

# %%
characters_count = "my father never liked me, but i forgive him"
count = len(characters_count.replace(" ", ""))
print("The characters without spaces are ", count)

# %%
a, b, c, d, e = 12, 11.1, 12, 12, 12
z = (a+b+c+d+e)/15
print(z)

# %%
# A program that calculates the GPA of USIU students offering computer courses
def Usiu_students_GPA(MTH1109, ENG11062, SUS1010, FIL1010, IST1020):
    GPA = (MTH1109 + ENG11062 + SUS1010 + FIL1010 + IST1020)/15
    return GPA
#Input for various students courses
MTH1109_str = input("Enter the marks you had for Algebra: ")
ENG1106_str = input("Enter the marks you had for English: ")
SUS1010_str = input("Enter the marks you had for SUS: ")
FIL1010_str = input("Enter the marks you had for Information literacy: ")
IST1020_str = input("Enter the marks you had for Information Systems: ")

#Check if the values can be converted to float
if MTH1109_str.isnumeric() and ENG1106_str.isnumeric() and SUS1010_str.isnumeric() and FIL1010_str.isnumeric() and IST1020_str.isnumeric():
    MTH1109 = float(MTH1109_str)
    ENG1106 = float(ENG1106_str)
    SUS1010 = float(SUS1010_str)
    FIL1010 = float(FIL1010_str)
    IST1020 = float(IST1020_str)

#Calculates and print results
    GPA = Usiu_students_GPA(MTH1109, ENG1106, SUS1010, FIL1010, IST1020)
    print(f"Your calculated GPA for the semester is: {GPA:.2f}")
    
# throw error when student enter  invalid input
else:
    print("Invalid input, Please check and enter a valid mark for the courses.")
    

# %%
# A program that calculates the GPA of USIU students offering computer courses
def Usiu_students_GPA(MTH1109, ENG11062, SUS1010, FIL1010, IST1020):
    GPA = (MTH1109 + ENG11062 + SUS1010 + FIL1010 + IST1020)/15
    return GPA

try:
#Input for various students courses
    MTH1109 = float(input("Enter the quality points you had for Algebra: "))
    ENG1106 = float(input("Enter the quality points you had for English: "))
    SUS1010 = float(input("Enter the quality points you had for SUS: "))
    FIL1010 = float(input("Enter the quality points you had for Information literacy: "))
    IST1020 = float(input("Enter the quality points you had for Information Systems: "))


#Calculates and print results
    GPA = Usiu_students_GPA(MTH1109, ENG1106, SUS1010, FIL1010, IST1020)
    print(f"Your calculated GPA for the semester is: {GPA:.2f}")
    
# throw error when student enter  invalid input
except ValueError:
    print("Invalid input, Please check and enter a valid value for the courses.")
    

# %%
#LIST
list = [0,1,2,3,4,5]

list[:3]

# %%
list1 = [1,2,3,4,5,6,7]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list[:])
print(list[-3:-1])
print(list[0:6:3])
print(list[:4])


