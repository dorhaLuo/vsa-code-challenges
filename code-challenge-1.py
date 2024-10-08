# Challenge 1 - greetings!
'''Using functions, write a “Get to know my classmate” program that asks 3-5 questions, 
allows answers to be provided via the console, and responds politely.

Be sure to comment your code
Be sure to test your code!

Optional Stretch goals:
Handle invalid input.

What happens if I just hit enter without typing anything?  
How should this be handled? How can you implement that?
'''


# defining functions
'''
INPUTS: None 
RETURNS: String: name (from user input)
PURPOSE: Greet the user by asking his/her name, then responding politely
'''
def greet_by_name():
    name = input("Hello! What's your name? ") # use input to get the name
    print("Nice to meet you, " + name + "! My name is Dorothy 罗清心🥰") # respond to the user with the input(name)
    return name # return the name so other functions can address the user by name

'''
INPUTS: String: name 
RETURNS: None
PURPOSE: Ask for the user's age, then respond politely
'''
def get_age(name):
    age = input("How old are you, " + name + "? ")
    print("Wow you're " + age + "! That's a great age!")

'''
INPUTS: String: name 
RETURNS: None
PURPOSE: Ask for the user's hobbies, then respond politely
'''
def get_hobbies(name):
    hobbies = input(name + ", what do you enjoy doing in your spare time? ")
    print("Ohhhh, " + hobbies + " sounds fun!")

'''
INPUTS: String: name 
RETURNS: None
PURPOSE: Ask for the user's location, then respond politely
'''
def get_location(name):
    location = input("Where do you live, " + name + "? ")
    print(location + "! Maybe I can visit you some day.")

'''
INPUTS: String: name 
RETURNS: None
PURPOSE: Tell the user we're having a game of Mad libs, then conduct the game
'''
def game_Mad_Lib(name):
    print("\n" + name + ", do you care for a game of Mad libs? ")

    noun = input("Give me a noun: ")
    emotion = input("Give me an emotion(noun): ")
    ing_verb = input("Give me a verb ending in ing: ")
    adjective = input("Give me an adjective: ")
    distance_with_unit = input("Give me a distance, complete with units: ")

    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''!!!!!! Please run the program before checking the next few lines of code! Please! Please! PLEASE! 🙈 !!!!!!'''
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    

    print("\nGuess what " + name + "? Yesterday I saw a " + adjective + " " + noun + ". It was " + ing_verb + " just " + distance_with_unit + " away from me!")
    print("You should have seen the look on my Granny's face, it was a look of sheer " + emotion + " ...")



# call the functions
# greet and get the name first, before calling the other functions
name = greet_by_name()  # assign the return from greet_by_name() into the variable name so that we can use it later 
get_age(name) # pass the argument into the function suite (hmmm... Did I use the terms correctly?)
get_hobbies(name)
get_location(name)

game_Mad_Lib(name)