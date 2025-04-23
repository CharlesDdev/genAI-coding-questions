# Write a function called `find_max`
# that takes a list of numbers as input
# and returns the largest number in the list (without using the built-in `max()` function).

def find_max(numslist):
    max_num = numslist[0]  # Start with the first element
    for num in numslist:
        if num > max_num:
            max_num = num  # Update if a larger number is found
    return max_num
