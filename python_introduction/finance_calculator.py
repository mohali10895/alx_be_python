# finance_calculator.py

# Step 1: Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))  # Get user input for income
monthly_expenses = float(input("Enter your total monthly expenses: "))  # Get user input for expenses

# Step 2: Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses  # Calculate savings

# Step 3: Project annual savings with a simple interest rate of 5%
annual_savings = monthly_savings * 12  # Total savings for the year
projected_savings = annual_savings + (annual_savings * 0.05)  # Add 5% interest

# Step 4: Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")  # Display monthly savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")  # Display projected savings
