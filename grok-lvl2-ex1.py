# Write a function called longest_word
# that takes two strings (words) as input
#  and returns the word that has more characters.
# If they’re the same length, return the first word.
# Use a loop to count the characters in each word (don’t use len()—just for practice!).

def longest_word(word1, word2):
    word1_tot = 0
    word2_tot = 0
    for char in word1:
        word1_tot += 1
    for char in word2:
        word2_tot += 1
    if word1_tot >= word2_tot:
        return word1  # Return the word, not the count
    else:
        return word2
