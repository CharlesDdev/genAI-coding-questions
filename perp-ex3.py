# Write a function called is_palindrome that takes a string as input
# and returns True if the string is a palindrome and False otherwise.
# When checking for a palindrome, ignore spaces, punctuation, and letter casing.
# For example:
	#	is_palindrome(“A man, a plan, a canal, Panama”) should return True.
	#	is_palindrome(“python”) should return False.

def is_palindrome(text):
    normalized = join(char.lower()
    for char in text:
        if char isalnum():
            return normalized
