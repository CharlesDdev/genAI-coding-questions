# Write a function called count_evens
# that takes three numbers as input and returns how many of them are even.
# Use a loop to check each number.
# Example:
# count_evens(2, 4, 7) → 2 (2 and 4 are even)

# count_evens(1, 3, 5) → 0 (no evens)

# count_evens(8, 10, 12) → 3 (all even)

def count_evens(num1, num2, num3):
    how_many_even = 0
    num_list = [num1, num2, num3]
    for num in num_list:
        if num % 2 == 0:
            how_many_even += 1
    return how_many_even
