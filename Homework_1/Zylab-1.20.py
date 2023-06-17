# Isaac Trevathan
# 1955674

# prompt user for number, get number
userNum = int(input('Enter integer:\n'))

# print out number
print('You entered:', userNum)

# function for squaring the user number
userNumSquared = userNum * userNum

# function for cubing the user number
userNumCubed = userNum * userNum * userNum

# print out the number squared
print(userNum, 'squared is', userNumSquared)

# print out the number cubed
print('And', userNum, 'cubed is', userNumCubed, '!!')

# prompt user for second number
userNum1 = int(input('Enter another integer:\n'))

# function to add first and second user numbers together
Add_Num = userNum + userNum1

# function to multiply first and second user numbers together
Multiply_Num = userNum * userNum1

# print the sum of the two numbers
print(userNum, '+', userNum1, 'is', Add_Num)

# print the product of the two numbers
print(userNum, '*', userNum1, 'is', Multiply_Num)
