# Question 2 (String with a Loop)
# You have this list: words = ["cat", "dog", "bird"].
# Write a for loop using range() and len() to:
# Print each word with its first letter capitalized
# OUTPUT: (e.g., "Cat").

words = ["cat", "dog", "bird"]

for values in range(len(words)):
    print(words[values].capitalize())
