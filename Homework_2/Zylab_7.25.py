# Isaac Trevathan
# 1955674

# creates fundtion for finding the amount of each coin, takes in user_total value as an argument
def exact_change(user_total):

    # sets each possible coin equal to zero
    dollars = 0
    quarters = 0
    dimes = 0
    pennies = 0
    nickels = 0

    # if the user total is greater than 100 it divides by 100 and uses the floor operator to get dollar amount
    if user_total >= 100:

        # sets dollars to the amount of dollars
        dollars = user_total // 100

        # subtracts the amount of cents from the dollars from the total
        user_total = user_total - ((user_total // 100) * 100)

    # if the amount of cents is greater than 25 it subtracts 25 for each quarter in the value from the total
    if user_total >= 25:
        while user_total >= 25:
            quarters += 1
            user_total -= 25

    # if the amount of cents is greater than 10 it subtracts 10 for each dime in the value from the total
    if user_total >= 10:
        while user_total >= 10:
            dimes += 1
            user_total -= 10

    # if the amount of cents is greater than 5 it subtracts 5 for each nickel in the value from the total
    if user_total >= 5:
        while user_total >= 5:
            nickels += 1
            user_total -= 5

    # if the amount of cents is greater than 1 it subtracts 1 for each penny in the value from the total
    if user_total >= 1:
        while user_total >= 1:
            pennies += 1
            user_total -= 1

    # returns the amount of coins for each type
    return dollars, quarters, dimes, nickels, pennies


if __name__ == "__main__":

    # gets user input value for the total
    input_val = int(input())

    # calls function for exact change using input_val as an argument and sets coin list equal to it
    coin_list = exact_change(input_val)

    # set the number of coin types equal to function exact_change for function check
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # checks if sum of all items in coin list is greater than zero
    if coin_list[0] + coin_list[1] + coin_list[2] + coin_list[3] + coin_list[4] > 0:

        # if dollar iis greater than zero
        if coin_list[0] > 0:

            # if there is only one dollar it prints 'dollar' else it prints 'dollars'
            if coin_list[0] == 1:
                print(coin_list[0], 'dollar')
            else:
                print(coin_list[0], 'dollars')

        # checks if greater than zero,if there is only one quarter it prints 'quarter' else it prints 'quarters'
        if coin_list[1] > 0:
            if coin_list[1] == 1:
                print(coin_list[1], 'quarter')
            else:
                print(coin_list[1], 'quarters')

        # checks if greater than zero,if there is only one dime it prints 'dime' else it prints 'dimes'
        if coin_list[2] > 0:
            if coin_list[2] == 1:
                print(coin_list[2], 'dime')
            else:
                print(coin_list[2], 'dimes')

        # checks if greater than zero,if there is only one nickel it prints 'nickel' else it prints 'nickels'
        if coin_list[3] > 0:
            if coin_list[3] == 1:
                print(coin_list[3], 'nickel')
            else:
                print(coin_list[3], 'nickels')

        # checks if greater than zero,if there is only one penny it prints 'penny' else it prints 'pennies'
        if coin_list[4] > 0:
            if coin_list[4] == 1:
                print(coin_list[4], 'penny')
            else:
                print(coin_list[4], 'pennies')

    # else it prints no change if there is no change
    else:
        print('no change')
