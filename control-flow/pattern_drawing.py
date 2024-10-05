# pattern_drawing.py

# Step 1: Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))  # Get user input

# Step 2: Initialize the row counter
row = 0

# Step 3: Draw the pattern using a while loop
while row < size:  # Iterate through rows
    for col in range(size):  # Iterate through columns
        print("*", end="")  # Print asterisk without a new line
    print()  # Print a newline character to move to the next row
    row += 1  # Increment the row counter
