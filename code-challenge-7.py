# With this challenge we continue working with our data structures. This challenge covers both Tuple and Set methods.

# Pay close attention to the instructions

# Use the following links for any help you need working with the methods
# https://www.w3schools.com/python/python_ref_tuple.asp
# https://www.w3schools.com/python/python_ref_set.asp

# I also expect you to use "trial and error" to investigate the following questions.

# For each method listed below, do the following:
# indicate any parameters the method takes,
# indicate the return value of the method
# provide an example for use.

# Here is the format I expect to see for each method. There should be a blank line before and after each response.

# methodName()
# @params: None/String/Integer/etc. This is what the method RECEIVES.
# @return: None/dict/int/etc
# Your own UNIQUE example of how to use it AND a sentence or two with a real world scenario where such a method would be useful.

############ TUPLES ###############
# https://www.w3schools.com/python/python_ref_tuple.asp

# count()
# @params: any type
# @return: int
# find how many swords we have
weapons = ("arrows","sword","bow","sword","spear","long bow", "sword")
sword_numb = weapons.count("sword")

# index()
# @params: any type (How many? 3?) (what if value not found? exception?)
# @return: int
# find the spear(imagine the weapons are stored in order)
weapons.index("spear")

# Explain why tuples have so few methods compared to lists, dictionaries and sets.
# Because tuples are immutable, you can't do much with them (not much manipulation).

############ SETS ###############
# https://www.w3schools.com/python/python_ref_set.asp

# add()
# @params: any type
# @return: None
# Imagine we are the Pevensies children in Narnia, and are going to a picnic. So, we go shopping for fruits. 
# We already have some in our basket, but we'd also like to try something new
fruits = {"apple", "banana", "cherry"}
fruits.add("durian")

# clear()
# @params: None
# @return: None
# It rained. Since the picnic is canceled, we're not going to buy so many food.
fruits.clear()

# copy()
# @params: None
# @return: set
# We decide we're going to have a banquet instead of a picnic. We're still going to need fruits
fav_fruits = {"apple", "banana", "cherry","peaches", "watermelon"}
banquet_fruits = fav_fruits.copy()

# discard()
# @params: any type (only 1)
# @return: None
# We want to remove durian just in case somebody sneaked it in(because we discovered Aslan doesn't like durian(sorry Aslan)=)
banquet_fruits.discard("durian")

# pop()
# @params: None
# @return: any type(removed item)
# We don't have enough room for all the fruits, so we need to pop something out.
# We'll pick randomly because we like every fruit and can't decide.
banquet_fruits.pop()

# remove()
# @params: any type
# @return: any type(removed item)
# the Chef is hungry, so she ate all the apples(which is her favorite)
banquet_fruits.remove("apple")

############### Built-in methods  #################
# https://www.w3schools.com/python/python_ref_functions.asp

# len()
# @params: an iterable(sequence or a collection)
# @return: int
# We want to know how many fruits we have left
fruit_num = len(banquet_fruits)

# sum()
# @params: iterable(of numbers only), start(optionals)
# @return: int or float
# We want to know how many guests are comming to our banquet
guests = {1,2,5,6,3,7,8,1,0,18,23,12,6,9,3,1,2}
num_of_guests = sum(guests)

# max()
# @params: an iterable, or one or more items to compare
# @return: any type
# At the banquet, we're haveing a game of comparing-numbers: find the largest number and win!
numbers = (10931903298210931, 19819819812398238923, 929498765432123456789) 
biggest_num = max(numbers)

# min()
# @params: an iterable, or one or more items to compare
# @return: any type
# We're haveing a game of comparing-numbers: find the smallest number and win!
numbers = (1.0931903298210931, 1.9819819812398238923, 1.929498765432123456789) 
smallest_num = min(numbers)

# sorted()
# @params: iterable, key(a func to decide the order, Optional), reverse = True|False (Optional)
# @return: sorted iterble(same type as the parameter)
# Sort the artists' last names in order, we want them to perform in reversed alphabetical order
# (the reverse action will happen in the next part)
artists = ["Smith","Brown","Foster","Roberts","Livingston","Wilder","Adams","Stevenson","Dickens"]
performers = sorted(artists)

# reversed()
# @params: an iterable object 
# @return: a (reversed) iterator object (what's an iterator object?)
# We want to print a performance programme
programme = reversed(performers)
n = 0
for each in programme:
    print(f"{n}: {each}")
    n = n + 1

# any()
# @params: iterable 
# @return: bool
# why does non-boolen values(ex. random letters) result in True?
# we conducted a pole to ask if anyone enjoyed the banquet
enjoyed = (True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True)
is_anyone_happy = any(enjoyed)

# all()
# @params: iterable
# @return: bool
# Mrs. Beaver wants to know if everything's still intact and good as new 
# -- all the table clothes and napkins and dresses and gowns and tapestries and draperies and etc.
# True = (no tears or holes)
intact = [True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True]
all_intact = all(intact) # Oh no! A False sneaked in, we have a spoiled table cloth😭


###########  OPTIONAL (SET METHODS)  ###########

# difference()
# @params: set (at least one)
# @return: set
# @shortcut: - 
# set_a – set_b = return values only existent in a (take out overlap with b from a)
# This is a flashback to before the banquet, still at the preparation stage, buying decorations.
# Susan has prepared us with a shopping list, and we have bought some things. In the process, we bought some other things (bc they seemed fitting/ or are good deal/ or for some other reasons).
# Mrs. Beaver wants to know what hadn’t been bought, to avoid buying anything twice
shopping_list = {"food", "fruits", "flowers", "decorations", "tapestries", "silverware", "napkins", 
                 "cleaning utensils", "invitations"}
Lucy_bought = {"napkins", "decorations", "candles", "little presents", "bowties", "necklaces"}
Edmund_bought = {"cleaning utensils", "invitations", "silverware", "cookware"}

what_remains = shopping_list - Lucy_bought - Edmund_bought # same as: remains = shop_l.defference(L_bought, E_bought)



centaur_approved = {"silverware", "napkins", "candles", "little presents", "bowties", "necklaces"} 

# intersection()
# @params: set (at least one)
# @return: set
# @shortcut: &
# Mr. Tumnus wants to find items that meet these requirements: 1. on the shopping list, 2. already procured, 3. approved by Oreius the Centaur
fill_requirements = shopping_list & Lucy_bought.union(Edmund_bought) & centaur_approved
# same as: fulfill = shopping_list.intersection( L.union(E), approved)


# isdisjoint()
# @params: set
# @return: bool
# Did Lucy and Edmund buy completely different thing?
no_repitition = Lucy_bought.isdisjoint(Edmund_bought)



MrsB_bought = {"flower","fruits","tapestries","food"}
bought = MrsB_bought.union(Lucy_bought, Edmund_bought) # all the things we bought combined

# issubset()
# @params: set
# @return: bool
# @shortcut: <= and < (what's the difference between the two?)
# Did we buy everything we need?
did_buy_all = shopping_list.issubset(bought) # everything on the shopping list was included in the items that were bought?


# issuperset()
# @params: set
# @return: bool
# @shortcut: >= and >
# Another way of checking if we bought everything
did_buy_all2 = bought >= shopping_list # we about more(or equal) than the items on the list


# symmetric_difference()
# @params: set
# @return: set
# @shortcut: ^
# anything that's not in both
# 


# union()
# @params: set (at least)
# @return: set
# @shortcut: |
# I did this earlier:
# Find how many things we bought in all
bought = MrsB_bought.union(Lucy_bought, Edmund_bought)



