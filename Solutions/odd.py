# Modify this code to a loop and tell a user if a number is even or odd.
# If the number is odd break out of the loop

# You can see an example output at Assignments/outputs/odd.png

while True:
    number = int(input("Enter number? "))

    if number % 2 == 0:
        print("This is an even number")

    else:

        print("This is an odd number,bye")
        break
