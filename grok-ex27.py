# Write a function count_a that takes a string
# and returns how many times the letter "a" appears.
# Use a loop.
# Example
# count_a("banana") → 3

#count_a("hi") → 0

def count_a(word):
    a_counter = 0
    for char in word:
        if char == "a":
            a_counter += 1
    return a_counter
