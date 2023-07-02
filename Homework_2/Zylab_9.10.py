# Isaac Trevathan
# 1955674

# imports csv
import csv

# gets user file
user_file = input()

# empty dictionary for later use
user_dict = {}

# sets j to zero
j = 0

# uses with and then open to open the file and close when finished. reads the file contents
with open(user_file, 'r') as my_file:

    # sets user_file_reader to reader for the csv file reader and sets the delimiter to ','
    user_file_reader = csv.reader(my_file, delimiter=',')

    # reads each row using the file reader
    for row in user_file_reader:

        i = 0

        # adds the row to the user dictionary if it is not already in dictionary it counts 1 in the dictionary
        # if the word is in the dictionary it adds to the value
        while i < len(row):
            if row[i] not in user_dict:
                user_dict[row[i]] = 1
            else:
                user_dict[row[i]] += 1
            i += 1

    # prints each dictionary key and vlue
    for key in user_dict:
        print(key, user_dict[key])
