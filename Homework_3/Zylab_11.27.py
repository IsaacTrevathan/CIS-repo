# Isaac Trevathan
# 1955674

# empty dictionary original_dict for later use
original_dict = {}

# empty list Jersey_list for later use
Jersey_list = []

# sets number_1 to number_5 equal to '100' for while loop check
number_1 = '100'
number_2 = '100'
number_3 = '100'
number_4 = '100'
number_5 = '100'

# sets rating_1 to rating_5 equal to '100' for while loop check
rating_1 = '100'
rating_2 = '100'
rating_3 = '100'
rating_4 = '100'
rating_5 = '100'

new_jersey = '100'
new_rating = '100'

# checks if the jersey number is in the range 0 99, gets input for number_1
while int(number_1) < 0 or int(number_1) > 99:
    number_1 = input('Enter player 1\'s jersey number:')

    if int(number_1) < 0 or int(number_1) > 99:
        print('please enter a number from 0 to 99')
print()

# checks if the rating number is in the range 1 to 9, gets input for rating_1
while int(rating_1) < 1 or int(rating_1) > 9:
    rating_1 = input('Enter player 1\'s rating:')
    if int(rating_1) < 1 or int(rating_1) > 9:
        print('please enter a number from 1 to 9')
print()

# adds number and rating to dictionary
original_dict[number_1] = int(rating_1)

# adds jersey number to Jersey_list
Jersey_list.append(int(number_1))
print()

# checks if the jersey number is in the range 0 99, gets input for number_2
while int(number_2) < 0 or int(number_2) > 99:
    number_2 = input('Enter player 2\'s jersey number:')
    if int(number_2) < 0 or int(number_2) > 99:
        print('please enter a number from 0 to 99')
print()

# checks if the rating number is in the range 1 to 9, gets input for rating_2
while int(rating_2) < 1 or int(rating_2) > 9:
    rating_2 = input('Enter player 2\'s rating:')
    if int(rating_2) < 1 or int(rating_2) > 9:
        print('please enter a number from 1 to 9')
print()

# adds number and rating to dictionary
original_dict[number_2] = int(rating_2)

# adds jersey number to Jersey_list
Jersey_list.append(int(number_2))
print()

# checks if the jersey number is in the range 0 99, gets input for number_3
while int(number_3) < 0 or int(number_3) > 99:
    number_3 = input('Enter player 3\'s jersey number:')
    if int(number_3) < 0 or int(number_3) > 99:
        print('please enter a number from 0 to 99')
print()

# checks if the rating number is in the range 1 to 9, gets input for rating_3
while int(rating_3) < 1 or int(rating_3) > 9:
    rating_3 = input('Enter player 3\'s rating:')
    if int(rating_3) < 1 or int(rating_3) > 9:
        print('please enter a number from 1 to 9')

# adds number and rating to dictionary
original_dict[number_3] = int(rating_3)

# adds jersey number to Jersey_list
Jersey_list.append(int(number_3))
print()
print()

# checks if the jersey number is in the range 0 99, gets input for number_4
while int(number_4) < 0 or int(number_4) > 99:
    number_4 = input('Enter player 4\'s jersey number:')
    if int(number_4) < 0 or int(number_4) > 99:
        print('please enter a number from 0 to 99')
print()

# checks if the rating number is in the range 1 to 9, gets input for rating_4
while int(rating_4) < 1 or int(rating_4) > 9:
    rating_4 = input('Enter player 4\'s rating:')
    if int(rating_4) < 1 or int(rating_4) > 9:
        print('please enter a number from 1 to 9')
print()

# adds number and rating to dictionary
original_dict[number_4] = int(rating_4)

# adds jersey number to Jersey_list
Jersey_list.append(int(number_4))
print()

# checks if the jersey number is in the range 0 99, gets input for number_5
while int(number_5) < 0 or int(number_5) > 99:
    number_5 = input('Enter player 5\'s jersey number:')
    if int(number_5) < 0 or int(number_5) > 99:
        print('please enter a number from 0 to 99')
print()

# checks if the rating number is in the range 1 to 9, gets input for rating_5
while int(rating_5) < 1 or int(rating_5) > 9:
    rating_5 = input('Enter player 5\'s rating:')
    if int(rating_5) < 1 or int(rating_5) > 9:
        print('please enter a number from 1 to 9')
print()
print()

# adds number and rating to dictionary
original_dict[number_5] = int(rating_5)

# adds jersey number to Jersey_list
Jersey_list.append(int(number_5))

# sorts Jersey_list
Jersey_list.sort()

# prints out ROSTER title
print('ROSTER')

# prints out jersey number and rating for each corresponding jersey in Jersey_list
for jersey in Jersey_list:
    print('Jersey number:', f'{jersey},', 'Rating:', original_dict[str(jersey)])
print()

# sets choose equal to '0'
choose = '0'

# checks if choose equals 'q'
while choose != 'q':

    # prints out choices menu
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()

    # gets choice input from user
    choose = input('Choose an option:')

    # checks if user input equals 'a'
    if choose == 'a':
        print()

        # gets input for new_jersey and checks if it is in range 0 to 99
        while int(new_jersey) < 0 or int(new_jersey) > 99:
            new_jersey = input('Enter a new player\'s jersey number')
            if int(new_jersey) < 0 or int(new_jersey) > 99:
                print('please enter a number from 0 to 99')
                print()

        print()

        # gets input for new_rating and checks if input is in the range 1 to 9
        while int(new_rating) < 1 or int(new_rating) > 9:
            new_rating = input('Enter the player\'s rating:')
            if int(new_rating) < 1 or int(new_rating) > 9:
                print('please enter a number from 1 to 9')
                print()

        # adds the key value pair to the dictionary original_dict
        original_dict[new_jersey] = int(new_rating)

        # adds the jersey number to Jersey_list
        Jersey_list.append(int(new_jersey))

        # sorts Jersey_list with the new jersey added in
        Jersey_list.sort()

    # checks if input is equal to d
    if choose == 'd':
        print()

        # gets jersey number from user
        print('Enter a jersey number:')
        delete_jersey = input()

        # deletes the jersey from Jersey_list
        Jersey_list.remove(int(delete_jersey))

        # deletes key value pair from the original_dict dictionary
        del original_dict[delete_jersey]

    # checks if choose is equal to 'u'
    if choose == 'u':
        print()

        # gets jersey number that is to be updated
        print('Enter jersey number')
        update_jersey = input()

        # gets new rating number
        print('Enter a new rating for player:')
        update_rating = input()

        # updates the dictionary with the new value for key
        original_dict[update_jersey] = update_rating

    # checks if choose equals 'o'
    if choose == 'o':
        print()
        print()

        # prints out ROSTER title
        print('ROSTER')

        # prints out jersey number and rating for each jersey
        for jersey in Jersey_list:
            print('Jersey number:', f'{jersey},', 'Rating:', original_dict[str(jersey)])
        print()

    # checks if choose == 'r'
    if choose == 'r':
        print()

        # gets user rating for comparison
        print('Enter a rating')
        user_rating = input()

        # prints out the jersey number and rating for all jerseys in Jersey_list that have a rating above user_rating
        print('ABOVE', user_rating)
        Jersey_list.sort()
        for jersey in Jersey_list:
            if original_dict[str(jersey)] > int(user_rating):
                print('Jersey number:', f'{jersey},', 'Rating:', original_dict[str(jersey)])
        print()

    # checks if choose == 'q'
    if choose == 'q':
        break
print()
