#  importing our own module
import our_module

# importing a variable from our module
from our_module import name_variable

username = input('Enter your username: ')

message_1 = our_module.greet(username)
print(message_1)

message_2 = our_module.greet("John")
print(message_2)

message_3 = our_module.greet(name_variable)
print(message_3)
