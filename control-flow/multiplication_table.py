# multiplication_table.py

# Step 1: Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))  # Get user input

# Step 2: Generate and print the multiplication table
for i in range(1, 11):  # Iterate through numbers 1 to 10
    product = number * i  # Calculate the product
    print(f"{number} * {i} = {product}")  # Print the result in the desired format
