# Write a function called cumulative_sum
# that takes a list of numbers as input
# and returns a new list where each element at index i is the sum of all input list elements from index 0 up to i.

def cumulative_sum(numslist):
    cumulative = []
    total = 0
    for num in numslist:
        total += num
        cumulative.append(total)
    return cumulative
