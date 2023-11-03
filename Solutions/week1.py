# Implement a program that prompts the user for the answer to the Great Question of Life, outputting Yes if the user inputs 36 or (case-insensitively) thirty-six or thity six. Otherwise output No.

# HINTS:
#     - No need to convert the user’s input to an int if you check for equality with "36", a str, rather 36, an int!

# Example output is at Assignments/outputs/week1.png


# inital solution
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


# fixed solution

# better naming convention used
# removed redundant code
answer_1 = 'thirty six'
answer_2 = 'thirty-six'
answer_3 = '36'
while True:

    user_answer = input("What's the answer to the Great Question of Life? ")

    if user_answer == answer_1 or user_answer == answer_2 or user_answer == answer_3:
        print('Yes')
        break
    else:
        print('No')


# a better solution
valid_answers = ['thirty six', 'thirty-six', '36']

while True:
    user_answer = input("What's the answer to the Great Question of Life? ")

    if user_answer in valid_answers:
        print('Yes')
        break
    else:
        print('No')
