# Isaac Trevathan
# 1955674

# int input for x coefficient 1
x_c_1 = int(input())
# int input for y coefficient 1
y_c_1 = int(input())
# int input for sum 1
sum_1 = int(input())
# int input for x coefficient 2
x_c_2 = int(input())
# int input for x coefficient 2
y_c_2 = int(input())
# int input for sum 2
sum_2 = int(input())

# sets x_answer = 0 for use later
x_answer = 0

# sets y_answer = 0 for use later
y_answer = 0

# sets solution = 0 for use later
solution = 0

# for x in the range of -10 to 11 it enters x into the formula
for x in range(-10, 11):

    # for y in the range of -10 to 11 it enters x into the formula
    for y in range(-10, 11):

        # checks if the x coefficient 1 times x, plus y coefficient 1 times y equals sum 1 and outputs into answer x
        # checks if the x coefficient 2 times x, plus y coefficient 2 times y equals sum 2 and outputs into answer y
        if ((x_c_1 * x) + (y_c_1 * y) == sum_1) and ((x_c_2 * x) + (y_c_2 * y) == sum_2):
            x_answer = x
            y_answer = y

            # sets solution equal to 1
            solution = 1

# prints answer if a solution was found, if not it prints No solution
if solution == 1:
    print(x_answer, y_answer)
else:
    print('No solution')
