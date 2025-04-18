# Write a function add_first_last that takes a list of numbers as input
# and returns the sum of the first and last numbers.
# Use a loop to find the last number (don’t use [-1]—just for practice!).
# Example:
# add_first_last([1, 2, 3]) → 4 (1 + 3)

# add_first_last([5]) → 10 (5 + 5)

# add_first_last([2, 4, 6, 8]) → 10 (2 + 8)

def add_first_last(numberslist):
    first = numberslist[0] # first number (no loop needed)
    last = 0 # placeholder for last
    for num in numberslist:
        last = num
    sum_of_eos = first + last # updates each time, keeps the last one
    return sum_of_eos
