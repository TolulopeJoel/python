# Implement a program that prompts the user for the answer to the Great Question of Life, outputting Yes if the user inputs 36 or (case-insensitively) thirty-six or thity six. Otherwise output No.

# HINTS:
#     - No need to convert the user’s input to an int if you check for equality with "36", a str, rather 36, an int!

# Example output is at Assignments/outputs/week1.png


question = '36'
answer = 'thirty six'

while True:

    user = input("What's the answer to the Great Question of Life? ")

    if user == question and answer:
        print('Yes')
        break

    elif user == answer:
        print('Yes')
        break

    else:
        print('No')