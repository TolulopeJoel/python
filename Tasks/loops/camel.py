# In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase.
# For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, or preferredFirstName.

# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase.
# For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

# In a this file, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

# HINT:
#     Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop
#     Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.


# OUTPUT:
#     Ouputs/camel.png

while True:
    user_input = input('camel case: ')
    snake_case = ''
    
    for char in user_input:
        if char == char.upper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    print(snake_case) 