
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04  

down_payment = portion_down_payment * total_cost


months = 0
monthly_salary = annual_salary / 12

while current_savings < down_payment:
    current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)
    months += 1

print("Number of months:", months)
