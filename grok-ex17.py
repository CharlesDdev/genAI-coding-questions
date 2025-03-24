# Write a function count_fives that takes a list of numbers as input and returns how many times the number 5 appears.
# Use a loop to check each number.
# Example:
# count_fives([1, 5, 3, 5]) → 2

# count_fives([2, 3, 4]) → 0

# count_fives([5]) → 1

def count_fives(numbers):
    how_many = 0
    for nums in numbers:
        if nums == 5:
            how_many += 1
    return how_many
