# Isaac Trevathan
# 1955674

# imports datetime module
from datetime import datetime

# creates dictionary for months with the amount of days in the month as the value for each
my_dictionary = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}


# defines a function word finder for searching a string for the date, and editing the format of the date
def word_finder(line, word):

    # creates variable k for loop
    k = 0

    # creates empty list for final output
    final_line = []

    # creates if statement that creates a minimum value for the size of the string
    if len(line) >= 10:

        # finds the location of the first letter of the argument 'word'
        word_location = line.find(word)

        # creates a new string that starts the location of the first letter of the argument 'word'
        new_string_1 = line[word_location:]

        # finds the location of the first space after 'word'
        space_location_1 = new_string_1.find(' ')

        # creates a string that contains the first word in new_string_1
        first_word = new_string_1[:space_location_1]

        # if statement that checks if the 'word' is not at the beginning of the string
        if word_location != 0:

            # checks if the character before the start of the argument 'word' is a space
            if not line[word_location - 1].isspace():

                # sets first_word to '0' if the character before 'word' is a space
                first_word = '0'

        # creates a string that starts at the location of the next word in the new_string_1
        new_string_2 = new_string_1[space_location_1 + 1:]

        # finds the location of the first space after the first word in new_string_2
        space_location_2 = new_string_2.find(' ')

        # creates a string that contains the first word in new_string_2
        second_word = new_string_2[:space_location_2]

        # creates and empty string for editing the second_word string later on
        new_second_word = ''

        # creates an empty list for joining different characters in to new_second_word later on
        second_word_list = []

        # creates a while loop that removes a comma from the end of second_word if there is one
        while k < len(second_word):

            # creates an if statement that occurs if there is a comma at the end of second word
            if second_word[-1] == ',' and second_word[0] != '0':

                # adds the different characters of second_word into a list if the character is not a comma
                if second_word[k] != ',':

                    # adds k to second_word_list
                    second_word_list.append(second_word[k])

                    # joins each list item of second_word_list into a new string new_second_word
                    new_second_word = ''.join(second_word_list)
            else:
                # sets new_second_word to string '0' if there is no comma at the end of second_word
                new_second_word = '0'

            # iterates k for the while loop
            k += 1

        # creates a new string that starts at the next word of new_string_2
        new_string_3 = new_string_2[space_location_2 + 1:]

        # sets third_word equal to the first for characters of new_string_3
        third_word = new_string_3[:4]

        # sets new_second_word_number equal new_second_word to be changed into an integer later
        new_second_word_number = new_second_word

        # sets k equal to zero
        k = 0

        # sets new_third_word equal to third_word
        new_third_word = third_word

        # while loop that checks the third_word for characters that are not a digit
        while k < len(new_third_word):

            # sets third_word to '0' if there is character that is not a digit
            if not new_third_word[k].isdigit():
                new_third_word = '0'
            k += 1

        # sets third_word_number equal to third_word to be changed into an integer
        third_word_number = new_third_word

        # checks if first word is equal to 'word' and checks if new_second_word_number is in the range of possible dates
        # checks if third_word_number is in the range of the possible years
        if first_word == word and 0 < int(new_second_word_number) < my_dictionary[word] and\
                0 < int(third_word_number) <= today_year_int:

            # adds first_word to final_line
            final_line.append(first_word)

            # adds new_second_word to final_line
            final_line.append(new_second_word)

            # adds third_word to final_line
            final_line.append(new_third_word)

    # returns the final line
    return final_line


# function that finds a word in a string and then returns the location in the string where the word ends
def end_finder(line_size, line, word):

    # finds the location of the start of the word in the string
    word_location = line.find(word)

    # if the word_location is not empty it sets word_end equal to the location of the end of the word
    if word_location != -1:
        word_end = word_location + len(word)

        # returns word end if word_location is not empty
        return word_end
    else:
        # returns the size of the original line if word_location is empty
        return line_size


# function to split a string based on spaces
def split(string):

    # splits strings based on spaces
    new = string.split(' ')

    # returns new (new list of string items)
    return new


# function to join elements of a list
def join(my_list):

    # joins elements of a list with a '/'
    new = '/'.join(my_list)

    # return new (new string made of list items)
    return new


# function that adds zeros to the beginning of each element of a list of numbers
def add_zeros(number):

    # creates a string zero = '0'
    zero = '0'

    # sets k to zero
    k = 0

    # creates empty list my_list
    my_list = []

    # while loop to check if the number is in the range of possible dates or years and add zeros to number
    while k < len(number):

        # sets value to k plus 1
        value = k + 1

        # checks if length of number list is less than 32 for days and not zero
        if len(number) < 33 and len(number) != 0:

            # checks if value is less than 10
            if value < 10:

                # adds one zero plus number to list
                my_list.append(zero + str(value))
            else:

                # adds number to list if it is lager than 10
                my_list.append(str(value))

        else:

            # if value is less than 10
            if value < 10:

                # adds 3 zeros and value to number list
                my_list.append(zero + zero + zero + str(value))

            # if value is less than 100
            elif value < 100:

                # adds 2 zeros and value to number list
                my_list.append(zero + zero + str(value))

            # if value is less than 1000
            elif value < 1000:

                # adds 1 zero and value to number list
                my_list.append(zero + str(value))

            # if value is less than todays year plus 1
            elif value <= today_year_int:

                # add value to number list
                my_list.append(str(value))

        # iterate k
        k += 1

    # my list
    return my_list


# function that makes a number list for each month
def month_num(my_months):

    # sets k to zero
    k = 0

    # empty list
    my_list = []

    # while loop that adds numbers for each list item
    while k < len(my_months):

        # adds number to the list
        my_list.append(k + 1)

        k += 1

    return my_list


# function that makes list of possible years
def list_max(my_max):

    # sets k to zero
    k = 0

    # creates empty list my_list
    my_list = []

    # creates while loop to add elements to the list with a total number of elements less equal to my_max
    while k <= my_max:

        # adds k to list
        my_list.append(k)

        # iterates k
        k += 1

    return my_list


# function to find month in a string
def find_month(string, my_months):

    # creates empty list to hold the location number of a month in a string later on
    location = []

    # for loop that adds the location to the list for each month in the list that is found
    for month in my_months:

        # adds location of month to list corresponding to the index that is equal to them number of the month (1 - 12)
        location.append(string.find(month))

    return location


def format_checker(input_list):

    # if split_string is an empty list it sets it equal to a list with 3 zeros ast elements
    if not input_list:
        input_list = [0, 0, 0]

    # checks if the first element of split_string is in the list of months
    # checks if the second element of split_string is in the range of possible days
    # checks if the third element of split_string is less than or equal to current year
    # checks if found is not zero or less
    if input_list[0] in months and int(input_list[1]) < 32 and int(input_list[2]) <= today_year_int:

        # if statement that occurs if the year found is less than the current year
        if int(input_list[2]) < today_year_int:

            # sets first element of split_string to the corresponding number with zeros added to single digits
            input_list[0] = user_month_value

            # sets second element of split_string to the corresponding number with zeros added to single digits
            # uses the value of split_string[1] as index to find number. subtracts 1 because index of list starts at 0
            input_list[1] = days_zeros[int(input_list[1]) - 1]

            # sets third element of split_string to the corresponding number, zeros added to years less than 4 digits
            # uses the value of split_string[2] as index to find number. subtracts 1 because index of list starts at 0
            input_list[2] = years_zeros[int(input_list[2]) - 1]

            # joins the elements of split string into as string called join_string
            join_string = join(input_list)

            # adds the string join_string to the list string_list for final output
            string_list.append(join_string)

        # if statement that occurs when the year is equal to the current year
        # checks if the month and day found are less than or equal to the current month and day
        elif int(input_list[2]) == today_year_int and found_month_digit <= today_month_int and \
                int(input_list[1]) <= today_day_int:

            # sets first element of split_string to the corresponding number with zeros added to single digits
            input_list[0] = user_month_value

            # sets second element of split_string to the corresponding number with zeros added to single digits
            # uses the value of split_string[1] as index to find number. subtracts 1 because index of list starts at 0
            input_list[1] = days_zeros[int(input_list[1]) - 1]

            # joins the elements of split string into as string called join_string
            # the third element of split_string is left unchanged
            # this is because if statement already checks that the third element is equal to the current year
            join_string = join(split_string)

            # adds join_string to the list string_list for final output
            string_list.append(join_string)
    # sets found back to zero to be used in next loop iteration


# opens file inputDates.txt and enters the contents into string user_content
with open('/Users/isaac/Desktop/DIS.txt', 'r') as my_file:
    user_content = my_file.read()


# sets time to the date and time of today
time = datetime.today()

# sets date to the date of today
date = time.date()

# changes the date of today into a string
today = str(date)

# splits the today string into parts based on the '-' character
today_split = today.split('-')

# sets today_year_number to the first element in today_split which is the current year
today_year_number = today_split[0]

# sets today_month_number to the first element in today_split which is the current month
today_month_number = today_split[1]

# sets today_day_number to the first element in today_split which is the current day
today_day_number = today_split[2]

# turns today_year_ number into an integer and sets today_year_int equal to it
today_year_int = int(today_year_number)

# turns today_month_ number into an integer and sets today_month_int equal to it
today_month_int = int(today_month_number)

# turns today_day_ number into an integer and sets today_day_int equal to it
today_day_int = int(today_day_number)

# creates an empty string user_input for user input later on
user_input = ''

# uses the list max function to create a list of days up to 31 and sets days equal to it
days = list_max(31)

# # uses the list max function to create a list of years up to the current year and sets 'years' equal to it
years = list_max(today_year_int)

# list of months called 'months'
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

# creates empty list string_list that is used to hold and output correct input dates later on
string_list = []

# uses the add zeros function to add zeros as the first character of single digit months
month_value = add_zeros(month_num(months))

# uses the add zeros function to add zeros as the first character of single digit days
days_zeros = add_zeros(days)

# uses the add zeros function to add zeros years with one, two, and three digits. Making four digit numbers
years_zeros = add_zeros(years)

# sets user_month_value to zero. this will be used to hold the value of the month found in the string
# this value will have a zero added if it is a single digit number
user_month_value = 0

# sets found_month_digit equal to zero. this is used to hold the digit of the month found later on
found_month_digit = 0
# sets found equal to zero. this is used to check if the month was found in the string later on
found = 0

# sets today_month_digit equal to zero. this will hold the month found in the string. this value does not have a zero
today_month_digit = 0

# empty string join_string that will be used to put day month and year into a string together


# empty list split_string that will be used to hold and check the correct ranges of the day month and year
split_string = []

# sets i equal to zero
i = 0

# while loop that continues for each of the 12 months
while i < len(months):

    # sets where equal to zero to be used later to locate the end of a found word
    where = 0

    # sets new_user_input equal to the user_content
    new_user_input = user_content

    while where < len(new_user_input):
        new_user_input = new_user_input[where:]

        # checks if the user input is string '-1'
        if user_input != '-1':

            # calls the word finder function to find the month and check the format of the date in the string
            # takes in the user_input string and every month out of 12 months
            # puts day month and year into list into list user_words if they are found
            split_string = word_finder(new_user_input, months[i])

            # checks if user words is an empty list
            if len(split_string) != 0:

                # sets user_month to the first item of the user_ words list
                user_month = split_string[0]

                # checks if there is a string for the user_month
                if split_string != -1:

                    # sets user_month_value to the value of the month that is found. this number has zeros added
                    user_month_value = month_value[i]

                    # calls month_num function
                    # sets month_digit to the list of values of the months. these numbers do not have zeros
                    month_digit = month_num(months)

                    # sets found_month_digit to the month that is found in the string
                    found_month_digit = month_digit[i]

                    # sets list split_string equal to user_words if the list user_words is not empty

                    format_checker(split_string)

        # sets input_length to the length of the string new_user_input
        input_length = len(new_user_input)

        # calls the end_finder function to find the end of the
        # sets where to the location where the found word ends in the string
        where = end_finder(input_length, new_user_input, months[i])

    # iterates i
    i += 1

# creates and or opens the file parsedDates.txt for writing
with open('parsedDates.txt', 'w') as my_file:

    i = 0

    # while loop that writes the items of string_list into into the file parsedDates.txt and add a new line for each
    while i < len(string_list):
        my_file.write(string_list[i])
        my_file.write('\n')

        # iterates i
        i += 1
