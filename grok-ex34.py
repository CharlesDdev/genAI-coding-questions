# Write a function longest_starts_with that takes two strings
# and returns the longer one, but only if it starts with the other string.
# If neither starts with the other, or they’re the same length, return the first string.
# Use loops (no startswith()).

# Example:
# longest_starts_with("cat", "catnip") → "catnip" (catnip starts with cat, longer)

# longest_starts_with("dog", "cat") → "dog" (no match)

# longest_starts_with("hi", "high") → "high" (high starts with hi, longer)

def longest_starts_with(word1, word2):
    len1 = 0
    for char in word1:
        len1 += 1
    len2 = 0
    for char in word2:
        len2 += 1
    starts_with_1 = True
    if len2 < len1:
        starts_with_1 = False
    else:
        for i in range(len1):
            pos = 0
            for char in word2:
                if char in word2:
                    if pos == i and char != word1[pos]:
                        starts_with_1 = False
                    pos += 1
    starts_with_2 = True # checks if word1 starts with word2
    if len1 < len2:
        starts_with_2 = False
    else:
        for i in range(len2):
            pos = 0
            for char in word1:
                if pos == i and char != word2[pos]:
                    starts_with_2 = False
                pos += 1
    if starts_with_1 and len2 > len1: # decides which to return
        return word2
    elif starts_with_2 and len1 > len2:
        return word1
    else:
        return word1
