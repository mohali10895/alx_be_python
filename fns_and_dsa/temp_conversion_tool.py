# temp_conversion_tool.py
# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Using the global conversion factor
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Using the global conversion factor
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Main user interaction function
def main():
    try:
        # Prompt user for input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Validate unit input and perform conversion
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.6f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.6f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function
if __name__ == "__main__":
    main()
