# Define a function get_grade(score)

'''Instead of printing, return the grade message

Call the function and store the result in a variable called result

Then print that result outside the function'''

def get_grade(score):
     
    if score >= 90:
        return "Grade: A - Excellent work!"
    elif score >= 80 and score <= 89:
        return "Grade: B - Good job!"
    elif score >= 70 and score <= 79:
        return "Grade: C - You passed."
    elif score >= 60 and score <= 69:
        return "Grade: D - Study more next time."
    else:
        return "Grade: F - You failed"
        
result = get_grade(85)
print(result)