# Write a function called sum_three
# that takes three numbers as input and returns their sum.
# Use a loop to add them up (even though you could just use +—just for practice!).
# Example:
# sum_three(1, 2, 3) → 6

# sum_three(5, 10, 15) → 30

# sum_three(0, 0, 0) → 0

def sum_three(int1, int2, int3):
    sum_of_all = 0
    numbers = [int1, int2, int3]
    for nums in numbers:
        sum_of_all += nums
    return sum_of_all
