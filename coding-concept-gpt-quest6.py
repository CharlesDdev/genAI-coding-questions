# Use your get_grade(score) function to determine if the student qualifies for the honor roll.

'''Keep your get_grade(score) function as-is — returning grade strings like "Grade: A - Excellent work!"

Ask the user for a score using input(), cast it to int

Call get_grade() with the score and store the result

Print the grade message

Then — if the grade includes an "A" or a "B", print:'''

def get_grade(score):
    if score >= 90:
        return "Grade: A - Excellent work!"
    elif 80 <= score <= 89:
        return "Grade: B - Good job!"
    elif 70 <= score <= 79:
        return "Grade: C - You passed."
    elif 60 <= score <= 69:
        return "Grade: D - Study more next time."
    else:
        return "Grade: F - You failed"

# Get input OUTSIDE the function
score = int(input("Enter your score from 0 to 100: "))

# Call the function and store result
result = get_grade(score)

# Print the result
print(result)

# Use logic based on returned grade
if "A" in result or "B" in result:
    print("Honor Roll: Yes")
else:
    print("Honor Roll: No")
