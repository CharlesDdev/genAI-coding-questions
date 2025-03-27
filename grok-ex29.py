# Write a function count_evens that takes a list of numbers
# and returns how many are even.
# Use a loop to check each number.
# Example:
# count_evens([1, 2, 3, 4]) → 2 (2 and 4)

# count_evens([1, 3, 5]) → 0

# count_evens([2]) → 1

def count_evens(numslist):
    how_many_evens = 0
    for num in numslist:
        if num % 2 == 0:
            how_many_evens += 1
    return how_many_evens
