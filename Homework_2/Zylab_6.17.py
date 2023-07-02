# Isaac Trevathan
# 1955764

# gets user password
password = input('Enter Password\n')

# adds q*s to the end of the password
password = password + 'q*s'

# creates empty list
my_list = []


# sets i to zero
i = 0

# sets x to empty string
x = ''

# checks each letter of the password for special letter and changes it to special character
while i < len(password):
    x = password[i]
    my_list.append(x)
    if my_list[i] == 'i':
        my_list[i] = '!'
    if my_list[i] == 'a':
        my_list[i] = '@'
    if my_list[i] == 'm':
        my_list[i] = 'M'
    if my_list[i] == 'B':
        my_list[i] = '8'
    if my_list[i] == 'o':
        my_list[i] = '.'

    # prints out the list items in one line
    print(f'{my_list[i]}', end='')
    i += 1
