# Isaac Trevathan
# 1955764

# function to get the age input form the user for values between 18 and 75 inclusive, returns the age
def get_age():
    age = int(input())

    # if the age is greater than 75 or less than 18 then a ValueError is raised
    if age > 75:

        raise ValueError()
    elif age < 18:
        raise ValueError()
    return age


# function for calculating the fat burning heart rate. Takes age as an argument. Returns heart_rate
def fat_burning_heart_rate(age):
    heart_rate = float(.70 * (220 - age))
    return heart_rate


if __name__ == "__main__":

    # sets up the try case for attempting to get the correct user input
    try:
        # calls get_age function and sets my_age equal to it
        my_age = get_age()

        # calls fat_burning_heart_rate and sets my_rate equal to it
        my_rate = fat_burning_heart_rate(my_age)

        # prints out the fat burning heart rate for the age entered by the user
        print('Fat burning heart rate for a', my_age, 'year-old:', '{:.1f}'.format(my_rate), 'bpm')

    # sets up the exception case for the invalid input into age
    except ValueError as excpt:

        # prints out that the input was invalid
        print('Invalid age.')
        print('Could not calculate heart rate info.')
        print()
