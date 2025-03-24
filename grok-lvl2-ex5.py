# Write a function called alternate_sum
# that takes a list of numbers as input and returns the sum of every other number,
# starting with the first one (index 0).
# Use a loop to do it.
# Example:
# alternate_sum([1, 2, 3, 4]) → 4 (1 + 3 = 4)

# alternate_sum([5, 10, 15]) → 20 (5 + 15 = 20)

# alternate_sum([2]) → 2 (just 2)

def alternate_sum(numbers):
    sum_of_every_other = 0
    for i in range(0, len(numbers), 2): # start at 0, step by 2
        sum_of_every_other += numbers[i] # adds every other number
    return sum_of_every_other
