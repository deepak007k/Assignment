annual_salary = float(input("Enter your starting annual salary: "))

total_cost = 1000000
portion_down_payment = 0.25
r = 0.04  
semi_annual_raise = 0.07  
down_payment = total_cost * portion_down_payment
months = 36
tolerance = 100  
low = 0
high = 10000
best_rate = (high + low) // 2
steps = 0

while low <= high:
    steps += 1
    portion_saved = best_rate / 10000
    current_savings = 0.0
    salary = annual_salary
    monthly_salary = salary / 12

    for month in range(1, months + 1):
        current_savings += (current_savings * r / 12) + (portion_saved * monthly_salary)

        if month % 6 == 0:
            salary += salary * semi_annual_raise
            monthly_salary = salary / 12

    if abs(current_savings - down_payment) <= tolerance:
        break  
    elif current_savings < down_payment:
        low = best_rate + 1
    else:
        high = best_rate - 1

    best_rate = (high + low) // 2

if low > high:
    print("It is not possible to save enough for the down payment in 36 months.")
else:
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", steps)
