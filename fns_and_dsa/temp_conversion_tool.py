TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F'
}

def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        else:
            return value
    else:
        return value

while True:
    # Prompt the user for input
    print('Enter the input temperature value:')
    value = float(input())
    print('Enter the input temperature scale (C, F):')
    input_scale = input().upper()
    print('Enter the output temperature scale (C, F):')
    output_scale = input().upper()

    # Convert the temperature and print the result
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    # Prompt the user to continue or quit
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break
