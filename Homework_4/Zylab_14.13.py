# Isaac Trevathan
# 1955674

# Global variable
num_calls = 0


# function to partition my_user_ids list
def partition(my_user_ids, i, k):

    # sets mid equal to i + (k-i) // 2 for midpoint
    mid = i + (k - i) // 2

    # sets pivot equal to my_user_ids value at index mid
    pivot = my_user_ids[mid]

    # sets done equal to False
    done = False

    # sets low equal to i for the low end of the partition
    low = i

    # sets h equal to k for the high end of the partition
    h = k

    # while loop that occurs until done equals true
    while not done:

        # while loop that adds 1 to low while my_user_ids at index low is less than pivot
        while my_user_ids[low] < pivot:
            low += 1

        # while loop that subtracts 1 from h while pivot is less than my_user_ids[h]
        while pivot < my_user_ids[h]:
            h -= 1

        # if low is greater than or equal to h, done is set equal to True
        if low >= h:
            done = True

        # if low is less than h, temp holds value for my_user_ids at index low
        # my_user_ids at index low is set equal to my_user_ids at index h
        # my_user_ids at index h equal is set equal to temp
        else:
            temp = my_user_ids[low]
            my_user_ids[low] = my_user_ids[h]
            my_user_ids[h] = temp

            # adds 1 to low
            low += 1

            # subtracts 1 from h
            h -= 1

    # returns h
    return h


# function to sort the values of my_user_ids using the quicksort method
def quicksort(my_user_ids, i, k):

    # gets global variable num_calls
    global num_calls

    # adds 1 to num_calls to count the number of times the function is used
    num_calls += 1

    # stops function call if i is greater than or equal to k
    if i >= k:
        return

    # calls partition function, sets j equal to the value of h returned by the function
    j = partition(my_user_ids, i, k)

    # calls the quicksort method, takes my_user_ids, i and k as arguments
    quicksort(my_user_ids, i, j)

    # calls the quicksort method, takes my_user_ids, j + 1 and k as arguments
    quicksort(my_user_ids, j+1, k)

    # stops function, ends recursion
    return


if __name__ == "__main__":

    # creates empty list user_ids
    user_ids = []

    # gets user input and sets user_id equal to it
    user_id = input()

    # appends user input into user_ids list while user input is not equal to -1
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
