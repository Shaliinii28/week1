'''
Name: Birashalynee Suthahar
Program: Temperature Converter
'''

def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the formula: (°C × 9/5) + 32
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the formula: (°F - 32) × 5/9
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    # Display menu options
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        # Get user's conversion choice
        choice = input("Enter choice (1 or 2): ").strip()

        # Check user's choice and if not correct print error message
        if choice not in ['1', '2']:
            print("Error: Invalid choice. Please select 1 or 2.")
            return

        # Get temperature input
        temp = input("Enter temperature: ").strip()
        temp = float(temp)  # Convert input to float

        # Perform conversion based on user's choice
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")  # Display result after conversion
        else:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")  # Display result after conversion

    except ValueError:
        # Check for invalid input
        print("Error: Please enter a valid number for temperature.")
    except Exception as e:
        # Check for other errors
        print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    # Run the converter function
    temperature_converter()