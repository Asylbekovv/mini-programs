import random
# Random number from at to
random_number = random.randint(1, 10)
print("Enter --> 'start' for begin program")
print("Enter --> 'stop' for exit from program")
while True:
    start_program_random = input("Enter your choice: ")
    if start_program_random == 'start':
        print(random_number)
    elif start_program_random == 'stop':
        print("Thank you dear user!")
        break
    else:
        print("Please your try again")
