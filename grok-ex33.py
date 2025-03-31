# Write a function sum_middle_three that takes a list of numbers
# (assume at least 3 items) and returns the sum of the three middle numbers.
# Use a loop to count the length (no len()), then sum the middle three.
# Example:
# sum_middle_three([1, 2, 3, 4, 5]) → 9 (2 + 3 + 4)

# sum_middle_three([10, 20, 30, 40, 50, 60]) → 90 (20 + 30 + 40)

# sum_middle_three([1, 2, 3]) → 6 (1 + 2 + 3)

def sum_middle_three(numslist):
    count = 0
    for num in numslist: # counts the length without len()
        count += 1
    start = (count - 3) // 2 # start of middle three
    middle_sum = 0
    pos = 0
    for num in numslist: # sum middle three
        if pos >= start and pos < start +3:
            middle_sum += num
    return middle_sum
