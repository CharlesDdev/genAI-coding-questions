# Write a function sum_first_five
# that takes a list of numbers and returns the sum of the first five numbers.
# If the list has fewer than five, sum all it has.
# Use a loop.
# Example:
# sum_first_five([1, 2, 3, 4, 5]) → 15 (1 + 2 + 3 + 4 + 5)

# sum_first_five([1, 2, 3]) → 6 (1 + 2 + 3)

# sum_first_five([10, 20, 30, 40, 50, 60]) → 150 (10 + 20 + 30 + 40 + 50)

def sum_first_five(numslist):
    five_added = 0
    count = 0
    for num in numslist:
        if count < 5:
            five_added += num
            count += 1
        else:
            break
    return five_added
