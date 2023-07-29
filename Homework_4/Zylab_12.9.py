# Isaac Trevathan
# 1955674

# Split input into 2 parts: name and age
parts = input().split()

# sets name to the first part of the
name = parts[0]

# while loop that continues until the user inputs '-1'
while name != '-1':

    # try case for adding 1 to the user age and printing name and age.
    try:
        # adds 1 to the age
        age = int(parts[1]) + 1

        # prints name and age
        print(f'{name} {age}')

        # Get next line
        parts = input().split()

        # sets name to first part of input
        name = parts[0]
        # occurs if the user string has a length larger than 1
        if len(parts) > 1:

            # checks if the age part of the user input is a digit
            if not parts[1].isdigit():

                # if the index 1 of parts is not a digit a Value Error is raised
                raise ValueError()

    # except case for the user input
    except ValueError as excpt:

        # sets age to zero if the user does not enter an age for the second word of the input
        age = 0

        # prints name and age
        print(f'{name} {age}')

        # splits name and age into a 2 part list
        parts = input().split()

        # sets name equal to the index 0 of the parts list
        name = parts[0]
