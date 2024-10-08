'''
Dorothy Luo
July 23 - July 24, 2024
Implement a more "advanced" calculator. Practice with loops, cases, conditionals, using user input, etc.
'''
# Calculator program Instructions
# take in user input
    # take in a number and validate that it is a number
    # require the user to re-enter if not a number
    # take in an operation and validate that it is a valid operation
# do the proper calculation
# print the answer
# allow user to continue to calculate until they say exit (need to check if they said exit)


'''"""FUNCTIONS SECTION"""'''


# this will be called after each user input
'''
INPUT: string
RETURN: boolean(TRUE/FALSE)
PURPOSE: Check if the parameter equals to "exit"(if so, return True)
'''
def is_exit(user_input): # "Check_if_exit"
    return user_input == "exit" # compare the strs and return T/F, work just like the conditionals below
    
    if user_input == "exit":
        return True
    else:
        return False
    
    pass # tells Python "leave me alone till later"
'''Test code
print(is_exit("exit")) # Expect this to be True
print(is_exit("not exit")) # FALSE 
'''


# this function will be called twice each time the calculator runs
'''
INPUT: a string
RETURN: boolean(TRUE/FALSE)
PURPOSE: Check if the number_input is an int (if so, return true)
'''
def is_valid_number(number_input): # "Check_if_valid_number"
    return number_input.isdigit() # only works for int, not for float, etc

'''
INPUT: a string
RETURN: boolean(TRUE/FALSE)
PURPOSE: Check if the number_input is a float (if so, return true)
'''
def is_valid_number_float(number_input):
    number_input = number_input.replace('.','', 1) # remove the first dot (decimal point)
    return number_input.isdigit() # check if the characters left are all numbers(int)
'''I searched, and there isn't a float-version of isdigit(). I can use try and except, but we haven't got to that yet
(I'm not sure how different it is from try-catch in C#). 
I got the idea for what I did in this function from stackoverflow: https://stackoverflow.com/questions/4138202/using-isdigit-for-floats
then I looked up the replace() method in w3schools: https://www.w3schools.com/PYTHON/ref_string_replace.asp'''


'''Test code
print(is_valid_number('4')) # True
print(is_valid_number('4.0')) # False, bc it's a float
print(is_valid_number_float('4.0')) # True, bc this func allows for floats
'''


'''
INPUT: a string
RETURN: boolean(TRUE/FALSE)
PURPOSE: Check if the operation_input is in the list of valid operations(if so, return true)
'''
def is_valid_operation(operation_input): # "Check_if_valid_operation"
    return operation_input in ['+','-','*','/'] # Is it in the list, T/F?


'''
INPUT: None
RETURN: None
PURPOSE: Greet the user
'''
def greeting():
    print("Hello, welcome to my calculator! ")
    print("Type 'exit' anytime to quit.\n")


'''
INPUT: None
RETURN: None
PURPOSE: Say goodbye to the user
'''
def goodbye():
    print("Thank you. Goodbye~")


# this is where I do the adding, subtracting, etc
# By the time calculate is called, I can trust that I have:
# two valid numbers and a valid operation
'''
INPUT: 2 integers and a string
RETURN: None
PURPOSE: print the calculated value
'''
def calculate(num_1, num_2, operation):
    if operation == '+':
        print(num_1 + num_2)
    elif operation == '-':
        print(num_1 - num_2)
    elif operation == '*':
        print(num_1 * num_2)
    elif operation == '/' and num_2 == 0:
        print("Sorry, division by 0 is not allowed :(")
    elif operation == '/':
        print(num_1 / num_2)
    else:
        print("Something is very very wrong") # Should never print
        # add the last else, even if you think it's really tight and water-proof


'''
INPUT: None
RETURN: None
PURPOSE: Kick start(run) the calculator, acting the Main(). 
'''
def start_calculator():
    greeting()
    
    while True: 
        # Repeatedly ask the user for a number until they provide a valid one
        num_1 = input("Enter your first number: ")
        
        while not is_valid_number_float(num_1):  # while input is not valid, keep asking
            if is_exit(num_1):
                goodbye() 
                return # quit the calc
                break # this will only break out of the "smaller" while loop
            num_1 = input("Enter your first number: ")
        

        # Do the above once again
        num_2 = input("Enter your second number: ")
        while not is_valid_number_float(num_2):
            if is_exit(num_2):
                goodbye() 
                return # quit the calc
            num_2 = input("Enter your second number: ")


        # Repeatedly ask the user for an operation until they provide a valid one
        op = input("Enter the operation['+','-','*','/']: ")
        while not is_valid_operation(op):
            if is_exit(op):
                goodbye() 
                return # quit the calc
            op = input("Enter the operation['+','-','*','/']: ")

        # cast into int(or float) and call calculate()
        calculate(float(num_1), float(num_2), op) 



# this is the function we call to run the calculator
start_calculator()
# goodbye() 
# we can call godbye() once if we put it here, it'll look nicer. 
# However, it's also nice to have one function that will make everything start(acting like a Main()). 
# Either is ok


# Learning Notes:
# Break all the features into functions to make the code easier to understand for code-reading
# another benefit: easier to find bug, bc we can test each function

# Test suites of code(functions) regularly, so as to find bugs and fix them asap

# Codeing does not has to be linear, start with any function