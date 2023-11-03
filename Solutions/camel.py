# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted.

# OUTPUT:
#     Ouputs/vowel.png

while True:
    user_input = input('camel case: ')  # user input case
    snake_case = ''
    
    for char in user_input:
        if char == char.upper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    print(snake_case) 