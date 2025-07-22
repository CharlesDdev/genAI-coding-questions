# Question:
# Write a program that takes a score (an integer from 0 to 100) and prints a message based on the grade:

'''90 or above → "Grade: A - Excellent work!"

80 to 89 → "Grade: B - Good job!"

70 to 79 → "Grade: C - You passed."

60 to 69 → "Grade: D - Study more next time."

Below 60 → "Grade: F - You failed."'''

score = int(input("Input your score (0 to 100) here:"))

if score >= 90:
    print("Grade: A - Excellent work!")
elif score >= 80 and score <= 89:
    print("Grade: B - Good job!")
elif score >= 70 and score <= 79:
    print("Grade: C - You passed.")
elif score >= 60 and score <= 69:
    print("Grade: D - Study more next time.")
else:
    print("Grade: F - You failed")