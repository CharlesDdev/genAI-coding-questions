# Your task is to write a function called `sum_of_list` that accepts a list of integers
# and returns the sum of all the integers.
# If the list is empty, your function should return 0.
# For example, given the list ``, the function should return `6`,
# and for an empty list `[]`, it should return `0`.

def sum_of_list(numslist):
    all_added_up = 0
    for num in numslist:
        all_added_up += num

    return all_added_up
