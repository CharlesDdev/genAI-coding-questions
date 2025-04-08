

def computepay():
    rate = float(input("Enter pay per hour: "))
    hrs_worked = float(input("Enter amount of hours worked: "))
    gross_pay = 0
    if hrs_worked <= 40:
        gross_pay = rate * hrs_worked
    elif hrs_worked > 40:
        gross_pay = (40 * rate) + ((hrs_worked - 40) * (1.5 * rate))
    return gross_pay

p = computepay()
print("Pay", p)
