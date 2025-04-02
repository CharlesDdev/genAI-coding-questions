# Write a function count_odds that takes a list of numbers
# and returns how many are odd.
# Use a loop.
# Example:
# count_odds([1, 2, 3, 4]) → 2 (1, 3)

# count_odds([2, 4, 6]) → 0

# count_odds([5]) → 1

def count_odds(numslist):
    how_many = 0
    for num in numslist:
        if num % 2 != 0:
            how_many += 1
    return how_many
