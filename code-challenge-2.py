'''
Dorothy Luo
July 22 - July 23, 2024
Implement a calculator. Practice with conditionals, using input, etc.
'''

# Create a calculator
# It only needs to run once (no need for a loop)
# Take user input for num_1, num_2 and operation
# Print the calculated value
# Assuming the user provides valid input
# valid operations [add, sub, mul, div]

# ask user for num_1
# ask user for num_2
# ask the user for an operation
# calculate


# Communicate with user, ask for input
num_1 = int(input("Please enter your first number: ")) # cast input_num into int
num_2 = int(input("Please enter your second number: "))
operation = input("Please enter an operation(add, sub, mul, div): ")

'''# test code
print(num_1.__class__) # tells me what type it is
print(num_2)'''

print("") # Extra line for formatting's sake

# Based on the user choice, print the results of the appropriate calculations
if operation == 'add':
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif operation == 'sub':
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif operation == 'mul':
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif operation == 'div':
    print(f"{num_1} / {num_2} = {num_1 / num_2}")
else:
    print("Sorry, you did not enter a valid operation. ")


# get the code working first
# then make it pretty and make it better
# test(run) code regularly, never wait till the program's finished

# pseudocode