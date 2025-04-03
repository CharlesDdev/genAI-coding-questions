# Print the length of the string (number or characters, including spaces)
# Use len()



def char_count():
    greeting = "good morning"
    char_total = 0
    for i in range(len(greeting)):
        char_total += 1
    return char_total

print(char_count()) # calls the function and prints it
