# Isaac Trevathan
# 1955674

def exact_change(user_total):
    dollars = 0
    quarters = 0
    dimes = 0
    pennies = 0
    nickels = 0

    if user_total >= 100:
        dollars = user_total // 100
        user_total = user_total - ((user_total // 100) * 100)

    if user_total >= 25:
        while user_total >= 25:
            quarters += 1
            user_total -= 25

    if user_total >= 10:
        while user_total >= 10:
            dimes += 1
            user_total -= 10

    if user_total >= 5:
        while user_total >= 5:
            nickels += 1
            user_total -= 5

    if user_total >= 1:
        while user_total >= 1:
            pennies += 1
            user_total -= 1

    return dollars, quarters, dimes, nickels, pennies


if __name__ == "__main__":
    input_val = int(input())
    coin_list = exact_change(input_val)
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if coin_list[0] + coin_list[1] + coin_list[2] + coin_list[3] + coin_list[4] > 0:

        if coin_list[0] > 0:
            if coin_list[0] == 1:
                print(coin_list[0], 'dollar')
            else:
                print(coin_list[0], 'dollars')

        if coin_list[1] > 0:
            if coin_list[1] == 1:
                print(coin_list[1], 'quarter')
            else:
                print(coin_list[1], 'quarters')

        if coin_list[2] > 0:
            if coin_list[2] == 1:
                print(coin_list[2], 'dime')
            else:
                print(coin_list[2], 'dimes')

        if coin_list[3] > 0:
            if coin_list[3] == 1:
                print(coin_list[3], 'nickel')
            else:
                print(coin_list[3], 'nickels')

        if coin_list[4] > 0:
            if coin_list[4] == 1:
                print(coin_list[4], 'penny')
            else:
                print(coin_list[4], 'pennies')
    else:
        print('no change')







