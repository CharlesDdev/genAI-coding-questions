#Write a function called max_of_three that takes three numbers as input
# and returns the largest one.
# Use a loop to compare them
# (don’t use max()—just for practice!).


def max_of_three(num1, num2, num3):
    numbers = [num1, num2, num3]
    max_num = numbers[0]  # Start with the first number
    for num in numbers:   # Check each number
        if num > max_num:  # If current number is bigger, update max
            max_num = num
    return max_num
