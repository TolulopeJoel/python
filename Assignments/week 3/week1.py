# Implement a program that prompts the user for the answer to the Great Question of Life, outputting Yes if the user inputs 36 or (case-insensitively) thirty-six or thity six. Otherwise output No.

# HINTS:
#     - No need to convert the user’s input to an int if you check for equality with "36", a str, rather 36, an int!

# Example output is at Assignments/outputs/week1.png


answer_1 = '36'
answer_2 = 'thirty six'
answer_3 = 'thirty-six'

while True:

    question = input("What's the answer to the Great Question of Life? ")

    if question == answer_1 or question == answer_2 or question == answer_3:
        print('Yes')
        break

    else:
        print('No')