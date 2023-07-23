# Isaac Trevathan
# 1955674

# imports datetime
from datetime import datetime

# imports csv
import csv


# creates DateInfo class
class DateInfo:

    # creates function to initialize class and variables
    def __init__(self, time, date, today, date_list, date_month_value, date_day_value):

        self.time = time
        self.date = date
        self.today = today
        self.date_list = date_list
        self.date_month_value = date_month_value
        self.date_day_value = date_day_value

    # function that gets today's date from datetime and splits it into a list
    def get_date(self):

        # sets time to the date and time of today
        self.time = datetime.today()

        # sets date to the date of today
        self.date = self.time.date()

        # changes the date of today into a string
        today = str(self.date)

        # splits the string 'today' into a list by the '-' character
        date_list = today.split('-')

        # returns the date_list
        return date_list

    # creates a function that compares the dates to today's date to check if date is passed due
    def passed_due_dates(self, user_items):

        # creates empty list 'passed_due_list for later use
        passed_due_list = []

        # sets the_date equal to a list containing today's date, obtained by the get_date function
        the_date = self.get_date()

        # for loop that iterates for each user item in the list user_items
        for element in user_items:

            # sets item_date equal to the index 4 of each element of user_items
            item_date = element[4]

            # sets item_string equal to item_date
            item_string = item_date

            # splits item_string by the '/' character and sets item_string_list equal to it
            item_string_list = item_string.split('/')

            # sets date_month_number equal to the month number in the month number in the_date
            date_month_number = the_date[1]

            # sets self.date_month_value equal to the date_month_number, removes any zeros prefixing the number
            # formats the value to zero decimal places
            self.date_month_value = '{:.0f}'.format((int(date_month_number) / 10) * 10)

            # sets date_day_number equal to the day value of the_date
            date_day_number = the_date[2]

            # sets self.date_day_value equal to the date_day_number, removes any zeros prefixing the number
            # formats the value to zero decimal places
            self.date_day_value = '{:.0f}'.format((int(date_day_number) / 10) * 10)

            # checks if the year value in item_string_list is less than the year value in the_date
            # if it is less then value is appended to passed_due_list
            if item_string_list[2] < the_date[0]:
                passed_due_list.append(element)

            # checks if the year value in item_string_list is equal to the year value in the_date
            # checks if the month value in item_string_list is less than the month value in the_date
            # if it is less then value is appended to passed_due_list
            if item_string_list[2] == the_date[0] and int(item_string_list[0]) < int(self.date_month_value):
                passed_due_list.append(element)

            # checks if the year and month values in item_string_list are equal to the year and month values in the_date
            # checks if the day value in item_string_list is less than the day value in the_date
            # if it is less then value is appended to passed_due_list
            if item_string_list[2] == the_date[0] and int(item_string_list[0]) == int(self.date_month_value) \
                    and int(item_string_list[1]) < int(self.date_day_value):
                passed_due_list.append(element)

        # returns passed_due_list
        return passed_due_list

    # function that formats today's date into the correct format for later use
    def format_date(self):

        # sets today_date equal to today's date, calls get_date function
        today_date = self.get_date()

        # creates a list to store the value of today's date in the correct format
        today_date_list = [int(self.date_month_value), int(self.date_day_value), int(today_date[0])]

        # returns today_date_list
        return today_date_list


# creates a function that finds all items in user_dict that are damaged
def get_damaged_items(user_dict):

    # creates empty list damaged_list to hold damaged items for later use
    damaged_list = []

    # for loop that iterates for each element in user_dict
    for element in user_dict:

        # sets my_item equal to the element in user_dict
        my_item = user_dict[element]

        # checks the index 5 of my_item to determine if the item is damaged
        if my_item[5] == 'damaged':

            # appends the value of user dict element to damaged_list
            damaged_list.append(user_dict[element])

    # returns damaged_list
    return damaged_list


# prompts user to input there file containing items
user_file = input('item file')

# sets i equal to zero for later use
i = 0

# creates empty list item_list for later use
item_list = []

# creates empty list manufacturer_list for later use
manufacturer_list = []

# creates empty dict manufacturer_dict for later use
manufacturer_dict = {}

# creates empty dict sorted_manufacturer_dict for later use
sorted_manufacturer_dict = {}

# creates empty dict manufacturer_count for later use
manufacturer_count = {}

# creates empyt dict prices_dict for later use
prices_dict = {}

# creates empty dict dates_dict for later use
dates_dict = {}

# creates empty dict damaged_dict for later use
damaged_dict = {}

# creates empty dict type_dict for later use
type_dict = {}

# creates empty list new_item_list for later use
new_item_list = []

# creates empty list type_name_list for later use
type_name_list = []

# creates empty list passed_date_list for later use
passed_date_list = []

# creates empty list earliest_item list for later use
earliest_item = []

# uses with and then open to open the file and close when finished. reads the file contents
with open(user_file, 'r') as my_file:

    # sets user_file_reader to reader for the csv file reader and sets the delimiter to ','
    user_file_reader = csv.reader(my_file, delimiter=',')

    # reads each row using the file reader
    for row in user_file_reader:

        # appends the contents of the row to item_list
        item_list.append(row)

    # sorts the elements of item_list
    item_list.sort()

# prompts the user to input the file containing item prices
user_file = input('price file')

# uses with and then open to open the file and close when finished. reads the file contents
with open(user_file, 'r') as my_file:

    # sets user_file_reader to reader for the csv file reader and sets the delimiter to ','
    user_file_reader = csv.reader(my_file, delimiter=',')

    # reads each row using the file reader
    for row in user_file_reader:

        # adds key value pair of item and price to prices_dict
        prices_dict[row[0]] = row[1]

# prompts user to input file containing the service dates of items
user_file = input('service dates file')

# uses with and then open to open the file and close when finished. reads the file contents
with open(user_file, 'r') as my_file:

    # sets user_file_reader to reader for the csv file reader and sets the delimiter to ','
    user_file_reader = csv.reader(my_file, delimiter=',')

    # reads each row using the file reader
    for row in user_file_reader:
        # adds key value pair of item and service date to prices_dict
        dates_dict[row[0]] = row[1]

# for loop that iterates for each item in item_list
for item in item_list:

    # creates a key value pair for the item and item type and adds it to type_dict
    type_dict[item[0]] = item[2]

    # checks if the item type is in type_name_list. if it is not in the list it is appended to type_name_list
    if type_dict[item[0]] not in type_name_list:
        type_name_list.append(type_dict[item[0]])

    # creates a key value pair of item number and damaged string, if 'damaged' is in the index 3 of the item
    # adds it to damaged_dict
    if item[3] == 'damaged':
        damaged_dict[item[0]] = item[3]

    # creates a key value pair of item number and empty 'damaged' string, if 'damaged' is not in the index 3 of the item
    # adds it to damaged_dict
    elif item[3] != 'damaged':
        damaged_dict[item[0]] = ''

    # removes 'damaged' string from item in item list to reformat later on
    if 'damaged' in item:
        item.remove('damaged')

    # removes empty 'damaged' string from item in item list to reformat later on
    elif '' in item:
        item.remove('')

    # appends the item price to the item in item_list
    item.append(prices_dict[item[0]])

    # appends the item service date to the item in item_list
    item.append(dates_dict[item[0]])

    # appends the item damaged value to the item in item_list
    item.append(damaged_dict[item[0]])

    # checks if manufacturer name is in manufacturer_list. if it is not it appends it
    if item[1] not in manufacturer_list:
        manufacturer_list.append(item[1])

    # checks if manufacturer name is in manufacturer_dict.
    # if not, it creates key value pair of manufacturer name and item information
    # creates key value pair of manufacturer name and number of occurrences and adds it to manufacturer_count
    if item[1] not in manufacturer_dict:
        manufacturer_dict[item[1]] = item
        manufacturer_count[item[1]] = 1

    # checks if manufacturer name is in manufacturer_dict.
    # if it is, it edits key value pair of manufacturer name and count to add 1 to the count number
    elif item[1] in manufacturer_dict:
        manufacturer_count[item[1]] += 1
        count_number = manufacturer_count[item[1]]

        # sets my_string equal to the manufacturer name of the item and adds the count number to the end of the string
        my_string = item[1] + str(count_number)

        # appends my_string to manufacturer_list
        manufacturer_list.append(my_string)

        # creates a key value pair of manufacturer name and item info and adds it to manufacturer_dict
        manufacturer_dict[my_string] = item

# for loop that checks if each item in manufacturer list is in manufacturer_dict
# uses the sorted order of manufacturer_list to sort the order of sorted_manufacturer_dict
# if item is in manufacturer_dict it creates key value pair of manufacturer name and item info
for item in manufacturer_list:
    if item in manufacturer_dict:
        sorted_manufacturer_dict[item] = manufacturer_dict[item]

# for loop that appends each item info for item in sorted_manufacturer_dict to new_item_list
for item in sorted_manufacturer_dict:
    new_item_list.append(sorted_manufacturer_dict[item])

# creates empty string for use in initializing DateInfo class instance
my_time = ''

# creates empty string for use in initializing DateInfo class instance
my_date = ''

# creates empty string for use in initializing DateInfo class instance
my_today = ''

# creates empty list for use in initializing DateInfo class instance
my_date_list = []

# creates empty string for use in initializing DateInfo class instance
my_date_month_value = ''

# creates empty string for use in initializing DateInfo class instance
my_date_day_value = ''

# creates instance of DateInfo class and sets date_instance equal to it
date_instance = DateInfo(my_time, my_date, my_today, my_date_list, my_date_month_value, my_date_day_value)

# calls get_date function to get today's date and sets my_date_list equal to it
my_date_list = date_instance.get_date()

# calls get_passed_due_dates function and sets late_dates equal to returned value, has new_item_list as argument
late_dates = date_instance.passed_due_dates(new_item_list)

# creates empty list final_passed_date_list for later use
final_passed_date_list = []

# creates empty list final_item_list for later use
final_item_list = []

# sets late_dates_length equal to the length of late_dates list
late_dates_length = len(late_dates)

# while loop that iterates for the length of late_dates
while i < late_dates_length:

    # calls format_date function and sets earliest_date_list equal to today's day month and year values
    earliest_date_list = date_instance.format_date()

    # for loop that iterates for each item in late_dates
    for item in late_dates:

        # uses index 4 of item to get date values and sets passed_date_item equal to it
        passed_date_item = item[4]

        # splits the date values in passed_date_item by '/' character and sets passed_date_list equal to it
        passed_date_list = passed_date_item.split('/')

        # checks if year value in passed_date_list is less than year value in earliest_date_list
        if int(passed_date_list[2]) < int(earliest_date_list[2]):

            # sets earliest_date_list equal to passed_date_list
            earliest_date_list = passed_date_list

            # sets earliest_item equal to item
            earliest_item = item

        # checks if month value in passed_date_list is less than month value in earliest_date_list
        # checks if year value in passed_date_list is equal to year value in earliest_date_list
        elif int(passed_date_list[0]) < int(earliest_date_list[0])\
                and int(passed_date_list[2]) == int(earliest_date_list[2]):

            # sets earliest_date_list equal to passed_date_list
            earliest_date_list = passed_date_list

            # sets earliest_item equal to item
            earliest_item = item

        # checks if day value in passed_date_list is less than day value in earliest_date_list
        # checks if month value in passed_date_list is is equal to month value in earliest_date_list
        # checks if year value in passed_date_list is equal to year value in earliest_date_list
        elif int(passed_date_list[1]) < int(earliest_date_list[1]) and int(passed_date_list[0]) == \
                int(earliest_date_list[0]) and int(passed_date_list[2]) == int(earliest_date_list[2]):

            # sets earliest_date_list equal to passed_date_list
            earliest_date_list = passed_date_list

            # sets earliest_item equal to item
            earliest_item = item

    # appends earliest_date_list to final_passed_date_list
    final_passed_date_list.append(earliest_date_list)

    # appends earliest_item to final_item_list
    final_item_list.append(earliest_item)

    # checks if earliest_item is in late_dates and removes earliest_item
    if earliest_item in late_dates:
        late_dates.remove(earliest_item)

    # iterates i
    i += 1

# calls get_damaged_items function and sets damage_items_list equal to it. uses sorted_manufacturer_dict as an argument
damaged_items_list = get_damaged_items(sorted_manufacturer_dict)

# empty list item_list_types for later use
item_list_types = []

# for loop that iterates for each item in new_item_list
for item in new_item_list:

    # sets item_list_no_type equal to item in new_item_list but removes the type value
    item_list_no_type = [item[0], item[1], item[3], item[4], item[5]]

    # appends item_list_types to with item_list_no_type
    item_list_types.append(item_list_no_type)


# for loop that iterates for each type in type_name_list
for name in type_name_list:

    # sets name_string equal to type name
    name_string = name

    # sets the type_file name equal to the type name and adds Inventory.csv to it
    type_file_name = name_string + 'Inventory.csv'

    # opens file with title type_file_name and writes items with that type into file
    with open(type_file_name, 'w') as type_inv:

        # for loop that iterates for each item in item_list_types
        for item_type in item_list_types:

            item_number = item_type[0]

            # checks if type name is in the item info
            if type_dict[item_number] == name:

                # joins elements of the item info in item_type by ' '
                type_string = ' '.join(item_type)

                # writes the item info into the file
                type_inv.write(type_string)

                # writes new line into the file
                type_inv.write('\n')

# sets i equal to zero
i = 0

# creates empty list order_price_list
order_price_list = []

# sets damaged_length equal to the length of damaged_items_list
damaged_length = len(damaged_items_list)

# creates empty list new_damaged_items
new_damaged_items_list = []

# creates empty list expensive_item
expensive_item = []

# while loop that iterates for the length of damaged_items_list
while i < damaged_length:

    # sets highest price equal to zero
    highest_price = 0

    # for loop that iterates for each item in damaged_items_list
    for item in damaged_items_list:

        # checks if the item price is higher that highest_price
        if int(item[3]) > int(highest_price):

            # sets highest_price equal to item price
            highest_price = item[3]

            # sets expensive_item equal to item
            expensive_item = item

    # appends new_damaged_items_list with expensive_item
    new_damaged_items_list.append(expensive_item)

    # removes expensive_item from damaged_items_list
    damaged_items_list.remove(expensive_item)

    # iterates i
    i += 1

# creates empty list final_damaged_items_list for later use
final_damaged_items_list = []

# for loop that appends each item in new_damaged_items to final_damaged_items but removes the damaged value from each
for item in new_damaged_items_list:
    damaged_items_no_damaged = [item[0], item[1], item[2], item[3], item[4]]
    final_damaged_items_list.append(damaged_items_no_damaged)

# opens Damaged.csv and writes item info for damaged items
with open('DamagedInventory.csv', 'w') as damaged:

    # iterates for each item in damaged_item_list
    for damage_item in final_damaged_items_list:

        # joins item info in item into string writ_string_damaged
        write_string_damaged = ' '.join(damage_item)

        # writes write_string_damaged into file
        damaged.write(write_string_damaged)

        # writes new line into file
        damaged.write('\n')

# opens PassedDates.csv and writes item info for items with service dates that are passed due
with open('PassedServiceDateInventory.csv', 'w') as passed_dates:

    # loop that iterates for each item in final_item_list
    for item in final_item_list:

        # joins item info in item by ' ' into string write_string_dates
        write_string_dates = ' '.join(item)

        # writes write_string_dates into file
        passed_dates.write(write_string_dates)

        # writes new line into file
        passed_dates.write('\n')

# opens FullInventory.csv and writes item info for items into file
with open('FullInventory.csv', 'w') as full_inv:

    # loop that iterates for each item in sorted_manufacturer_dict
    for item in sorted_manufacturer_dict:

        # joins item info in item by ' ' into string write_string
        write_string = ' '.join(sorted_manufacturer_dict[item])

        # writes write_string into file
        full_inv.write(write_string)

        # writes new line into file
        full_inv.write('\n')
