# match_case_calculator.py

# Prompt user for the first number
num1 = float(input("Enter the first number: "))

# Prompt user for the second number
num2 = float(input("Enter the second number: "))

# Prompt user for the operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform the calculation using a match case statement
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")
