# Write a function sum_odds that takes a list of numbers as input
# and returns the sum of all odd numbers in the list.
# Use a loop to check each number.
# Example:
# sum_odds([1, 2, 3, 4]) → 4 (1 + 3 = 4)

# sum_odds([2, 4, 6]) → 0 (no odds)

# sum_odds([5, 7]) → 12 (5 + 7 = 12)

def sum_odds(numbers):
    odd_nums = [] # collect all odds in list
    for nums in numbers:
        if nums % 2 != 0: # checks if odd
            odd_nums.append(nums)
    odd_nums_sum = sum(odd_nums_sum) # sums at end **(notice the indentation)
    return odd_nums_sum
