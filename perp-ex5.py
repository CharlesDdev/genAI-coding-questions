def count_vowels(words):
    vowels = "aeiouAEIOU"
    count = 0
    for char in words:
        if char in vowels:
            count += 1
    return count
