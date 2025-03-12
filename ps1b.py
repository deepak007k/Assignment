# ps1b.py
# Author: Your Name
# Collaborators: (List any collaborators here)

# Get user input
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Constants
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04  # Annual return rate

# Compute required down payment
down_payment = portion_down_payment * total_cost

# Calculate the number of months needed
months = 0
monthly_salary = annual_salary / 12

while current_savings < down_payment:
    current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)
    months += 1

    # Increase salary every 6 months
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12

# Print result
print("Number of months:", months)
