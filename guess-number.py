'''
Dorothy Luo(partner Linyi Li)


'''

# Guess a number game
# code-challenge-8
import random


'''
@param: none
@return: none
@purpose: Print greetings and the rules'''
def greeting():
    print("\n________________________________________________________________________________________\n")
    print("Greetings! We're having a number-guessing game, please answer with arabic numbers. " + 
          "\nYou only have 5 chances, use them wisely." +
          "\nEnter 'exit' to quit the game~ \n")


'''
@param: None
@return: None 
@purpose: print to the user, indicate the game has indeed ended'''
def goodbye():
    print("\nGoodbye, have a good day!")
    print("________________________________________________________________________________________\n\n")


'''
@param: None
@return: int 
@purpose: generate a random number'''
def generate_random():
    return random.randint(1,100) # both included


'''
@param: int
@return: bool 
@purpose: evaluate whether the inputed int is greater than 0 (user has any chances left)'''
def have_chance(guess_No):
    return guess_No > 0 # there are guesses left


'''
@param: string
@return: bool 
@purpose: evaluate whether the inputed string equals to 'exit' '''
def want_exit(user_input):
    return user_input == 'exit'


'''
@param: string
@return: bool 
@purpose: check if the inputed string is a number (accept ints AND floats)'''
def is_number(number_input):
    number_input = number_input.replace('.','', 1) # remove the first dot (decimal point), replace with ''(nothing)
    return number_input.isdigit() # check if the characters left are all numbers(int)


'''
@param: string, int
@return: bool 
@purpose: evaluate if the two parameter are equal in number'''
def correct_guess(user_input, random_number):
    return float(user_input) == random_number

'''
@param: string, int, int
@return: None
@purpose: compare the number value of the string and the first int, then print statements accordingly'''
def large_or_small(user_input, random_number, tracker):
    user_input = float(user_input) # convert to a number
    if user_input < random_number: # compare
        if tracker == 1:
            print(f"Too small, guess larger. Only 1 guess left.") # for the sake of grammar
        else:
            print(f"Too small, guess larger. {tracker} guesses left.") # notify user
    else:   # guess > random_number
        if tracker == 1:
            print(f"Too large, guess smaller. Only 1 guess left.")
        else:
            print(f"Too large, guess smaller. {tracker} guesses left.")


'''
@param: none
@return: none 
@purpose: contain all the other functions, starts the game once this function is called'''
def start_game():
    greeting()

    while True:
        tracker = 5 # tracks the number of guess the user has left
        random_num = generate_random() # generate the random number
        
        while have_chance(tracker):  # aka. ask-for-guesses loop
            
            while True:  # aka validity-check loop

                user_guess = input("Enter your guess:   ")
                if want_exit(user_guess):
                    goodbye()
                    return # quit the start_game function(guit the whole game)
                elif is_number(user_guess):
                    tracker = tracker - 1  # one less chance
                    break
                else:
                    print("!! Previous input is invalid, guess again!!")
            
            # we now have a valid guess
            if correct_guess(user_guess,random_num):
                if tracker == 4:  
                    print(f"Congratulations! The random number WAS {random_num}. You only used 1 guess! That's incredible!!!")
                else:
                    print(f"Congratulations! The random number WAS {random_num}. You only used {5 - tracker} guesses!")
                break # stop asking for more guesses

            else:
                large_or_small(user_guess, random_num, tracker) # compare guess and random_number, then give user feedback
        

        # By now either the user has guessed correctly, or he ran out of guesses

        # if no chances left AND did not guess correctly
        if not have_chance(tracker) and not correct_guess(user_guess, random_num):
            print(f"Sorry, you lost:( You ran out of guesses, the random number was {random_num}).")
        
        # only exit when user says 'n'
        choice = input("Do you want to play again? (y/n):  ")
        if choice == 'n': # don't want to play again
            break # quit the topmost while loop(the game's about to end)
        else:
            print("\nWonderful! Let's do it again!")
            print("________________________________________________________________________________________\n\n")
            # continue looping through the game
    
    goodbye()


# call the "Big" function and start the game
start_game()