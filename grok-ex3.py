# Question 3 (Loop Review)

# You have this list: nums = [4, 7, 2, 9, 5].
# Write a for loop using range() and len() to:
# Count how many numbers are odd.

# Print the count at the end.

nums = [4, 7, 2, 9, 5]
odd_count = 0

for values in range(len(nums)):
    if nums[values] % 2 != 0:
        odd_count += 1
print(odd_count)
