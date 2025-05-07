def main():
    filename = "user_input.txt"

    # Get user input
    user_input = input("Enter some text: ")

    # Save to file (creates new file if it doesn't exist)
    try:
        with open(filename, 'w') as file:
            file.write(user_input)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

    # Read from file
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("File contents:")
        print(content)
    except FileNotFoundError:
        # This case won't occur since we just created the file
        print(f"File {filename} was just created and contains your input")
    except Exception as e:
        print(f"Error reading from file: {e}")

if __name__ == "__main__":
    main()