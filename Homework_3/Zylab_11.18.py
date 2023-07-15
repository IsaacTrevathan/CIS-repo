# Isaac Trevathan
# 1955674

# gets input from user
my_input = input()

# splits user input by the spaces, creates my_list
my_list = my_input.split(' ')

# creates empty list final_list for later use
final_list = []

# creates empty list int_list for later use
int_list = []

# for loop that appends the number in my_list to int_list if the number is not negative
for number in my_list:
    if int(number) >= 0:
        int_list.append(int(number))

# sorts the int_list items
int_list.sort()

# for loop that appends the number in int_list to final_list
for number in int_list:
    final_list.append(str(number))

# joins the elements in final_list to string final_string
final_string = ' '.join(final_list)

# outputs final_string ending with a space
print(final_string, end=' ')
