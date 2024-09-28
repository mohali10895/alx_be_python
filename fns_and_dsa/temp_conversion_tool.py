# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR\s*=\s*9\/5    # Factor to convert Celsius to Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Calculate Celsius from Fahrenheit
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Calculate Fahrenheit from Celsius
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main user interaction function
def main():
    try:
        # Prompt user for input temperature
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
