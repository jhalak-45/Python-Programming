# Assigning values to variables
name = "Ram Bahadur"
age = 25
height = 5.5
is_student = True

# Printing variable values
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# Legal variable names
myvar = "Ram"
my_var = "Ram"
_my_var = "Ram"
myVar = "Ram"
MYVAR = "Ram"
myvar2 = "Ram"

# Illegal variable names:

# 2myvar =  "Hello Nepal"
# my-var =  "Hello Nepal"
# my var = "Hello Nepal"

# techniques to make them more readable
# 1. Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "Hello Nepal"

# 2. Pascal Case
# Each word starts with a capital letter:
MyVariableName =  "Hello Nepal"

# 3. Snake Case
# Each word is separated by an underscore character:
my_variable_name =  "Hello Nepal"

# Many Values to Multiple Variables
x, y, z = "C++", "Python", "C"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Python"
print(x)
print(y)
print(z)
# Unpack a Collection
languages = ["Python", "C++", "C"]
x, y, z = languages
print(x)
print(y)
print(z)


# Global Variables

global_var = "Good Programming Language"

def myfunc():
    local_var= "Programming Language"
    print("Python is " + global_var)
    print("Python is " + local_var)
myfunc()
print(global_var)
# print(local_var) #this occur error because, the loacl_var is local variable it works only inside myfunc()
