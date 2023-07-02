# Isaac Trevathan
# 1955674

# gets user string
user_string = input()

# splits user string based on spaced
split_string = user_string.split(' ')

# joins the list items from split_string together
join_string = ''.join(split_string)

# join the items of split string together with spaces in between
join_string_2 = ' '.join(split_string)

# sets i = 0
i = 0

# sets error to zero for later use
error = 0

# for x in the range 0 to the length of the joined string it checks if the first letter of the string equals the last
for x in range(0, len(join_string)):
    if join_string[0 + i] != join_string[-1 - i]:

        # adds plus one to error if there is an instance where the first and last letters do not match and breaks loop
        error += 1
        break
    i += 1

# prints the string join_string and 'is not a palindrome' if an error was found. prints 'is a palindrome' if no error
if error > 0:
    print(join_string_2, 'is not a palindrome')
elif error < 1:
    print(join_string_2, 'is a palindrome')
