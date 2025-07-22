# Question
# Define a function called grade_score(score)

'''Move your grading logic inside the function

Instead of asking for input inside the function, just pass in the score

Test it with different values: grade_score(95), grade_score(67), etc.'''

def grade_score(score):
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
        
grade_score(85)