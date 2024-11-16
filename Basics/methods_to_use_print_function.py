# Methods for Formatting and Displaying Output Using Python's print() Function Alongside Other Functions
a = 10
b = 10.5
c = "python programming"

# Method 1: Pass multiple variables directly
# You can pass multiple variables to the print function, separated by commas.
print(a, b, c)  
# and 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Output: 10 10.5 python programming

# Method 2: Print variables with descriptive text
# You can print descriptive text along with the variables for clarity.
print("value of a:", a)  
# Output: value of a: 10
print("value of b:", b)  
# Output: value of b: 10.5
print("value of c:", c)  
# Output: value of c: python programming

# Method 3: Print variables individually
# Each variable can be printed individually on a new line.
print(a)  
# Output: 10
print(b)  
# Output: 10.5
print(c)  
# Output: python programming

# Method 4: Using old style string formatting (% operator)
# You can format strings using the old-style `%` operator, specifying the data type.
print("value of a: %d" % a)  
# Output: value of a: 10
print("value of b: %.1f" % b)  
# Output: value of b: 10.5
print("value of c: %s" % c)  
# Output: value of c: python programming

# Method 5: Using f-strings (Python 3.6+)
# f-strings allow embedding expressions directly within string literals using curly braces {}.
print(f"value of a: {a} and value of b: {b}, value of c: {c}")  
# Output: value of a: 10 and value of b: 10.5, value of c: python programming
print(f"value of b: {b}")  
# Output: value of b: 10.5
print(f"value of c: {c}")  
# Output: value of c: python programming

# Method 6: Using .format() method
# The .format() method provides another way to format strings.
print("value of a: {}".format(a))  
# Output: value of a: 10
print("value of b: {}".format(b))  
# Output: value of b: 10.5
print("value of c: {}".format(c))  
# Output: value of c: python programming

# Method 7: Using the end parameter
# The end parameter lets you control what is printed at the end of the output, replacing the default newline.
print(a, end=" | ")  
print(b, end=" | ")  
print(c)  
# Output: 10 | 10.5 | python programming

# Method 8: Using sep parameter
# The sep parameter allows you to specify a separator between multiple variables in print.
print(a, b, c, sep=", ")  
# Output: 10, 10.5, python programming

# Method 9: Concatenating variables and strings using the + operator
# You can concatenate strings and variables using the + operator, but variables need to be converted to strings.
print("value of a: " + str(a))  
# Output: value of a: 10
print("value of b: " + str(b))  
# Output: value of b: 10.5
print("value of c: " + c)  
# Output: value of c: python programming

# Method 10: Using repr() for debugging (Print raw representation)
# repr() provides a detailed representation of the object, useful for debugging.
print(repr(a))  
# Output: 10
print(repr(b))  
# Output: 10.5
print(repr(c))  
# Output: 'python programming'

# Method 11: Printing to a file
# You can redirect the output of print to a file by specifying the file parameter.
with open("output.txt", "w") as f:
    print(a, b, c, file=f)
# Output: This will save "10 10.5 python programming" into the file output.txt

# Method 12: Using rjust(), ljust(), and center() for alignment
# These methods allow you to format strings with padding and alignment.
print(str(a).rjust(5))  
# Output: '   10' (right-aligned with padding)
print(str(b).ljust(10))  
# Output: '10.5      ' (left-aligned with padding)
print(c.center(30))  
# Output: '       python programming       ' (centered with padding)

# Method 13: Printing Unicode characters
# You can print Unicode characters using escape sequences.
print("Unicode heart: \u2665")  
# Output: Unicode heart: ♥
print("Unicode smiley: \U0001F600")  
# Output: Unicode smiley: 😀

# Method 14: Multiline printing using triple quotes
# Triple quotes allow you to print multiline strings easily.
print("""This is a
multiline
print statement""")
# Output:
# This is a
# multiline
# print statement

# Method 15: Printing a dictionary or list in a readable format using pprint
# For complex data structures like dictionaries, use pprint for better readability.
import pprint
data = {'a': a, 'b': b, 'c': c}
pprint.pprint(data)
# Output: {'a': 10, 'b': 10.5, 'c': 'python programming'}
