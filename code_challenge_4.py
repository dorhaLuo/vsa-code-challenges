'''
Dorothy Luo
July 25 - , 2024
Purpose: learn and practice with List and Dictionary methods. Attempt at learning by oneself(directly from written instructions references)
'''

# For this code challenge you will interact with List and Dictionary methods.

# This Code Challenge will be autograded. Your code MUST pass the tests in order to receive full credit. I will also be visually inspecting your code to ensure you are using the List and Dictionary methods to produce the expected output.

# NOTE:
# 1. At no point should you use input()
# 2. You can and should manually test each method by calling the method with the expected starting value. Your method calls are NOT needed to pass the tests. (Each test will call your method). 
# 3. All tests will run each time you "Run Tests"
# 4. Work from top to bottom. Some of the methods require the return value from a prior method, so do not jump around. Solve the first problem, get that test passing, then work on the second problem.
# 5. You may use the following resource to help you identify the correct List/Dictionary method to use, and find examples for how to use them:

# Dictionaries: https://www.w3schools.com/python/python_ref_dictionary.asp
# Lists: https://www.w3schools.com/python/python_ref_list.asp

# This is a solo assignment. No collaboration is allowed. Learn to read code examples from the above links and using experimentation and trial & error, work through each test and resolve each error you face.

# Each function below is looking for 1 specific list or dictionary method.

# You have the skills needed to do this!

# Remember to put your name, date and summary of the purpose of your code at the top of this file as a comment before submitting.


# List

# return an empty list
'''
Input: None
Return: 1 list(empty)
Purpose: learn to create a list
'''
def create_list():
  return []
  a_list = [] # left it here since is this a documentation of my learning process
  return a_list # which method is more recommended?


# create a list. 
# use the append() method three times to add three names to your list.
# return the list
'''
Input: None
Return: a list
Purpose: learn to add(append) objects to a list
'''
def append_list():
  name_list = []
  name_list.append("Alina")
  name_list.append("Bethany")
  name_list.append("Cadence")
  return name_list


# Return a COPY of this list
'''
Input: a list
Return: a list(a copy of the original)
Purpose: learn to use the copy() function
'''
def copy_list(my_list):
  return my_list.copy()
  new_copy_list = my_list() # left it here since is this a documentation of my learning process
  return new_copy_list

# Use the following list:
# num_list = [15, 11, 43, 32, 11, 23, 11]
# return how many times the number 11 appears in this list
'''
Input: a list
Return: an int
Purpose: learn to use the count() function
'''
def count_list_length(my_list):
  return my_list.count(11)


# FOR THE REMAINING FUNCTIONS:
# You will reuse the same list. Pay close attention to the instructions.

# list to use: 
fruit_list = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"]
# Return a sorted version of this array. It should be sorted in ascending order
'''
Input: a list
Return: a list
Purpose: learn to use the sort() function
''' # *tripped here* Tried to: return my_list.sort()
def sort_list(my_list):
  my_list.sort()
  return my_list


# using the return value from sort_array to test. This function should return a reversed list. 
'''
Input: a list
Return: a list
Purpose: learn how to reverse a function
'''
def reverse_list(my_list):
  my_list.sort(reverse = True)
  return my_list


# Starting from your SORTED array:

# insert 'Papaya' such that it is the 3rd element in the list. 
  # Remember that lists start from index 0
  # Return the list 
'''
Input: a list
Return: a list
Purpose: learn to use the insert() function
'''
def insert_papaya(my_list):
  my_list.insert(2,"papaya")
  return my_list

#######################################################################################################################
# fruit_list = ["pear", "apple", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"] # original
# fruit_list = insert_papaya(fruit_list)
# fruit_list = ["pear", "apple", "papaya", "peaches", "pineapple", "bananas", "cherries", "oranges", "kiwi"] # should look like this after the insert_papaya() function
#######################################################################################################################

# using your list after calling insertPapaya to test, 'pop' the 5th ELEMENT.
# return the amended list
'''
Input: a list
Return: a list
Purpose: learn to use the pop() function
'''
def pop_five(my_list):
  my_list.pop(4)
  return my_list


# using your list after calling insertPapaya, allow user to indicate which index to remove. Return the popped item
'''
Input: a list and an int
Return: an object(allows for any type, probably a string in our case)
Purpose: learn to access an object in a list, then use the pop() function to delete it
'''
def pop_element(my_list, index_number):
  poping_item = my_list[index_number]
  my_list.pop(index_number)
  return poping_item


###############  DICTIONARY METHODS   ##############

my_dict = {
  'Alabama': 'Southeast',
  'California': 'West',
  'Maine': 'New England',
  'Ohio': 'Midwest',
  'Arizona': 'South'
}

# Use the above dictionary to test the following methods

# Return all keys for the dictionary
'''
Input: a dictionary
Return: a list
Purpose: learn how to get a list of the keys of a dictionary
'''
def get_keys(my_dict):
  return my_dict.keys()
  key_list = my_dict.keys()
  return key_list


# For any key passed in, return the corresponding value
'''
Input: a dictionary and a key(of the dictionary)
Return: a value
Purpose: learn how to get a value using a key
'''
def get_value(my_dict, key):
  return my_dict.get(key)


# update the value for key 'Arizona' to say 'Southwest'
'''
Input: a dictionary, a key, and an object(probably a string in our case)
Return: a dictionary
Purpose: learn how to update/add to a dictionary
'''
def update_dict(my_dict, key, new_value):
  my_dict.update({key:new_value})
  return my_dict

# print(update_dict(my_dict, 'Arizona', 'Southwest'))
