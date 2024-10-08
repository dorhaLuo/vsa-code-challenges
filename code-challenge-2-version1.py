'''
Dorothy Luo
July 22 - 
Implement a calculator. Practice with loops, conditionals, using input, etc.
'''

# Instructions: Implement a calculator. 
# Create a function that takes in 3 parameters: number_1, number_2, operation to perform 
# [ add, sub, mul, div ]
# Ask the user to enter the values and operation that they want to calculate.
# Print the answer to the screen.
# Allow user to continue making calculations (use a loop) until they say "quit"
# 
#  Your program will be tested with the following:
#       3, 4, add. (output should be 7)
#       5, 3, sub  (output should be 2)
#       10, 4, mul (output should be 40)
#       45, 5, div (output should be 9)
 

# OPTIONAL: After passing all 4 tests, if you want a challenge:
# What happens if you enter a string instead of a number? How can you fix that?
## What happens if you enter an operation other than the 4 specified? How can you fix it?
## Does anything funky happen when you divide? What? How can you adjust? What if the numbers do not divide evenly?

'''FOLLOW THE REQUIREMENTS! LETTER BY LETTER'''
 
 # Pseudocode

 # I need to create a loop that takes in user input
 #  The loop asks user for three inputsL number_1, number_2, operation
 # if the user says "quit" at any time, I exit the loop

 # Store the user inputs into variables
 #      example: 1, 2, add
 # create a menu
 #  1. Addition
 #  2. Subtraction
 #  3. Multiplication
 #  4. Division 
 #  5. Exit
 # Use conditionals to determine what operation is wanted (add, sub, mul, div)
 # Based on the conditional, compute the equation and print the value
 # call functions 

'''
INPUT: None
RETURN: str
PURPOSE: display a menu to the user, ask & recieve desired input
'''
def options_menu():
    while 1==1: # loop endlessly, unless: user enters a valid number -> a value is returned -> breaks out of the function(and in doing so, breaks out of the loop) 
        ''' Menu Method 1
        # better fits the practicing-with-lists-purpose, but I like mythod2(use a lot of print()) better because it looks neater =D
        print("Please select the desired operation: ")
        for each in ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Quit"]:
            print(each) 
        '''

        # communicate to the user
        # print a menu of options
        print("Please select the desired operation: ")
        print("1. Addition") # add sub mul div 
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        choice = input() # recieve user input
        
        # map the choice(a number) to the appropriate operation and return it
        print("") # add an extra line for formatting purposes
        if choice == '1':
            return "add"
        elif choice == '2':
            return "sub"
        elif choice == '3':
            return "mul"
        elif choice == '4':
            return "div"
        elif choice == '5':
            return "quit"
        else:
            print("Sorry, there has been an error. Please enter an arabic number from 1 to 5")

    

    # Instruction Notes:
    #   keep asking for input until the value entered is valid
    #   if the user selects 1, you map that to add 
    #   so that if -else is looking at if str =="add"


'''
INPUT: None
RETURN: None (return null to jump out of the loop)
PURPOSE: The main program, runs continually
'''
def get_user_input():
    while 1==1: # will loop endlessly, untill: user picks 'quit' -> breaks out of the function with return(and in doing so, breaks out of the loop)
        print("\nWelcome to the \"Endless\" Basic Calculator!")
        number_1 = int(input("Please enter your first number: ")) # cast the input into an int
        number_2 = int(input("Please enter your second number: "))
        operation = options_menu() # options_menu() returns a string

        # 1. check if user wants to quit and provide a polite message if they do, 
        #     and use return to quit the function
        # 2. otherwise, use if-elif-else to compute the equation and print the value
        if operation == "quit":
            print("Thank you. Goodbye! ")
            return
        elif operation == "add":
            print(f"{number_1} + {number_2} = {number_1 + number_2}") # prints the equation
        elif operation == "sub":
            print(f"{number_1} - {number_2} = {number_1 - number_2}")
        elif operation == "mul":
            print(f"{number_1} * {number_2} = {number_1 * number_2}")
            # handling division by 0
            if number_2 == 0:
                number_2 = int(input("For division, the second number cannot be 0. Please enter another number: "))
                print("") # add an extra line for formatting purposes

            print(f"{number_1} / {number_2} = {number_1 / number_2}")
        else:
            print("Sorry, there has been an error. Please try again. ")




    
    
get_user_input() # Call the function