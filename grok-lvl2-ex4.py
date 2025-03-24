# Write a function called ends_same that takes two strings as input
# and returns True if they end with the same character,
# and False otherwise.
# Use a loop to find the last character of each string
# (don’t use [-1]—just for practice!).
#
# Example:
# ends_same("cat", "rat") → True (both end with “t”)

# ends_same("hello", "hi") → False (o ≠ i)

# ends_same("dog", "frog") → True (both end with “g”)

def ends_same(word1, word2):
    last1 = ""
    last2 = ""
    for char in word1:
        last1 = char
    for char in word2:
        last2 = char
    if last1 == last2:
        return True
    else:
        return False
