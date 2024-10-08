# This code challenge is a mirror image of what we did verbally in class with List method. 
# You will repeat the same steps, but with dictionary methods. 

# Pay close attention to the instructions

# Use the following link for any help you need working with the methods
# https://www.w3schools.com/python/python_ref_dictionary.asp

# I also expect you to use "trial and error" to investigate the following questions.

# For each method listed below, do the following:
# indicate any parameters the method takes,
# indicate the return value of the method
# provide an example for use.

# Here is the format I expect to see for each method. There should be a blank line before and after each response.

# methodName()
# INPUT: None/String/Integer/etc. This is what the method RECEIVES. 
# RETURN: None/dict/int/etc
# Your own UNIQUE example of how to use it AND a sentence or two with a real world scenario where such a method would be useful. 
# For example, "The dictionary holds student information for each class, with student names as the key, and information about that student as the value. The last student who enrolled in the class decided to drop the class. I can use popitem() to remove that last enrollment. "
# Your example does not have to be perfect, but it must demonstrate that you are thinking about HOW each method is used.

messy_info_sheet = {"weight": "lighter than me 😭", "name" : "I don't know", "height" : "0.0", "age" : "forgotten", 
                    "sport event" : "what’s for dinner?", "details" : "O.o"} # Syntax is messy on purpose
# for a sports game (somewhat like the Olympics perhaps)


# clear()
# INPUT: None
# RETURN: None
# A sleepy intern confusedly typed up an info sheet. Then she took a nap, woke up, and cleared the mess.
messy_info_sheet.clear()


names = {"Alina", "Bethany", "Cadence", "Derik", "Ella", "Fitzroy", "Gisela"}

# copy()
# INPUT: None
# RETURN: dictionary
# make a copy of the names of the players. Use the copy to record scores (later)
players = names.copy()


# fromkeys()
# INPUT: keys, value(Optional)
# RETURN: dictionary
# create a score board using the players’ names and the initial score of 0
# using {set} as keys will not keep the order, but (tuple) will
score_board = dict.fromkeys(players, 0)


# get()
# INPUT: keyname, object of any type(Optional, value to return if keyname doesn’t exist)
# RETURN: any type
# get the score. If the player’s not found, say “player not found”
one_score = score_board.get("Biana", "player not found")


# items()
# INPUT: None
# RETURN: dict_items (key-value pairs as tuples in a list)
# We want an ordered list of the current scores in pair with the player names
# We want to be able to control the order later
player_score_pair = score_board.items()
score_board["Biana"] = 0
print(player_score_pair)


# keys()
# INPUT: None
# RETURN: a view object as a list
# We want to see how many players are left (we’re at the quarterfinal now)
quarterfinal_players = score_board.keys()
print(quarterfinal_players) ###########



# pop()
# INPUT: keyname, default value(Optional, value to return if keyname doesn’ exist)
# RETURN: any type (popped value)
# Continuing on to the semifinal, 4 players had been defeated. They need to be removed
score_board.pop("Ella")
score_board.pop("Biana")
score_board.pop("Bethany")
score_board.pop("Cadence")


score_board["Gethan"] = 100

# popitem()
# INPUT: None
# RETURN: any type (popped value)
# Somebody tried to worm his way into the semifinal through his connections, 
# but the rules won’t let him slip
scoundrel = score_board.popitem() # pop him out AND catch him


# setdefault()
# INPUT: keyname, value(Optional, becomes keyname’s value if keyname doesn’t exist. Default value None)
# RETURN: any type (keyname’s value)
# The scoundrel wanted to replace Gisela, we want to check if Gisela’s records are still in the system
G_records = score_board.setdefault("Gisela", 70)


# update()
# INPUT: dictionary or iterable with key:value pairs (what’s an iterable with key:value pairs?)
# RETURN: None
# We want to update the scores
score_board.update({"Fitzroy": 83})
score_board.update({"Alina":85})
score_board.update({"Gisela":84})
score_board.update({"Derick":84})


# update()
# INPUT: dictionary or iterable with key:value pairs (what’s an iterable with key:value pairs?)
# RETURN: None
# We want to update the scores
score_board.update({"Fitzroy" : 83})
score_board.update({"Alina" : 85})
score_board.update({"Gisela" : 84})
score_board.update({"Derick" : 84})


# values()
# INPUT: None
# RETURN: view object as a list
# We want to see how the players are doing (see their scores)
purely_scores = score_board.values()