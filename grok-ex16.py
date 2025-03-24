# Write a function called all_positive
# that takes three numbers as input
# and returns True if all of them are positive (greater than 0),
# and False if any are zero or negative.
# Use a loop to check them.

def all_positive(num1, num2, num3):
    numbers = [num1, num2, num3]
    for nums in numbers:
        if nums <=0:
            return False
    return True
