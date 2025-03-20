# Question 5 (String with a Loop)

# fruits = ["apple", "banana", "kiwi"]

#Use a for loop with range() and len()
# print fruits with 5 or more letters, in uppercase.

fruits = ["apple", "banana", "kiwi"]

for actual_values in range(len(fruits)):
    if len(fruits[actual_values]) >= 5:
        print(fruits[actual_values].upper())
