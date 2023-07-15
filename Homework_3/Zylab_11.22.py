# Isaac Trevathan
# 1955674

# gets input from user
user_input = input()

# splits user_input by the spaces
user_list = user_input.split(' ')

# creates empty list for later use
my_list = []

# creates empty dictionary for later use
my_dictionary = {}

# sets i to 0
i = 0

# while loop that iterates over the length of user_list
while i < len(user_list):

    # if user_list item is not int my_list it appends the item to my_list
    if user_list[i] not in my_list:
        my_list.append(user_list[i])

        # crates a key: value  for dictionary equal to 1
        my_dictionary[user_list[i]] = 1

    # if the user_list item is found in my_list it adds 1 to the value in the key value pair
    elif user_list[i] in my_list:
        my_dictionary[user_list[i]] = my_dictionary[user_list[i]] + 1

    # iterates i
    i += 1

# sets i equal to zero
i = 0

# prints each word in the user_list and outputs the number of times each word appears in the list
while i < len(user_list):
    print(user_list[i], my_dictionary[user_list[i]])
    i += 1
