# Write a function sum_numbers_from_user that:
# Asks the user to input a list of numbers separated by spaces (e.g., "1 2 3").

# Splits the input into a list and sums the numbers using a loop.

# Returns the sum. (Assume valid number inputs for now.)

# Example:
# User types "1 2 3" → 6

# User types "10 20" → 30

# User types "5" → 5

# Hint: Use input().split() to turn "1 2 3" into ["1", "2", "3"], then convert strings to ints.

def sum_numbers_from_user():
    user_input = input("Enter a list of numbers separated by a space to see their sum: ")
    number_list = user_input.split() # ["1", "2", "3"]
    new_list_summed = 0
    for num in number_list:
        new_list_summed += int(num) # Convert each string to int
    return new_list_summed
