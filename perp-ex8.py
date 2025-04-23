# Write a function called `unique_elements`
# that takes a list as input
# and returns a new list
# containing only the unique elements from the original list,
# preserving their original order.

def unique_elements(numslist):
    unique_list = []
    for num in numslist:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
