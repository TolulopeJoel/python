# random module

import random


# for i in range(11):
#     random_number = random.randint(1, 100)
#     print(random_number)

fruits = ['apple', 'orange', 'cherry', 'grape']

#  select an item at random
random_fruit = random.choice(fruits)
print(random_fruit)

print(fruits)

# shuffle
random.shuffle(fruits)

print(fruits)


# dice

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

dice = (die1, die2)

print(dice)
