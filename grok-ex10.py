# Write a function called is_even
# that takes a number as input and returns True if the number is even, and False if it’s odd.
# You don’t need a loop for this one—just use a simple condition.
# Example OUTPUT:
# is_even(4) → True

# is_even(7) → False

# is_even(0) → True

def is_even(integer):
    if integer % 2 == 0:
        return True
    if integer % 2 != 0:
        return False
