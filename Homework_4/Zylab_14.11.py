# Isaac Trevathan
# 1955674

# function for selection sorting the argument num_list
def selection_sort_descend_trace(num_list):

    # for loop that iterates over the length of num_lsit
    for i in range(len(num_list)):

        # sets the max index value equal to i
        max_index = i

        # for loop that iterates over the length of num_list -1. This is achieved by starting the range at i + 1
        for j in range(i + 1, len(num_list)):

            # if num_list at index j is larger than num_list at index max_index, max_index is set equal to j
            if num_list[j] > num_list[max_index]:
                max_index = j

        # temp is set equal to num_list at index i as a temporary placeholder for value swithching
        temp = num_list[i]

        # num_list at index i is set equal to num_list at index max_index
        num_list[i] = num_list[max_index]

        # num_list at index max_index is set equal to temp
        num_list[max_index] = temp

        # if i is less than the length of num_list - 1 each number in num_list is outputted followed by a space
        if i < len(num_list) - 1:
            for element in num_list:
                print(element, end=' ')
            print()


if __name__ == "__main__":

    # gets input from user and splits it into list items by the ' '
    my_list = (input().split(' '))

    # creates empty list number_list for later use
    number_list = []

    # adds each number in my_list into number_list
    for item in my_list:
        number = int(item)
        number_list.append(number)

    # calls the selection_sort_descend_trace function to sort the numbers from greatest to smallest
    # takes number_list as an
    selection_sort_descend_trace(number_list)
