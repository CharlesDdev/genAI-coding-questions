# Write a function first_is_big that takes a list of numbers
# and returns True if the first number is greater than 5, False otherwise.
# Use a loop to get the first number (no list[0]—just for practice!).
# Example:
# first_is_big([6, 2, 3]) → True (6 > 5)

# first_is_big([4, 7, 8]) → False (4 ≤ 5)

# first_is_big([10]) → True (10 > 5)

def first_is_big(numslist):
    for num in numslist:
        if num > 5:
            return True # first number wasn't > 5
    return False # empty list case
