'''
Name: Birashalynee Suthahar
Program: Simple login system
'''

# Sample user database
users = {
    "shalu": "alienworld3",
    "aru": "flowerland5@",
    "hellodd": "samplename@"
}

def login(username, password):
    # Check if username exists and password matches
    if username in users and users[username] == password:
        return True
    return False

def login_system():
    max_attempts = 3
    attempts = 0

    print("Simple Login System")
    
    while attempts < max_attempts:
        try:
            # Get user input
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            # Input validation
            if not username or not password:
                print("Error: Username and password cannot be empty.")
                attempts += 1
                print(f"Attempts remaining: {max_attempts - attempts}")
                continue

            # Login attempt
            if login(username, password):
                print(f"Welcome, {username}! Login successful.")
                return
            else:
                print("Error: Invalid username or password.")
                attempts += 1
                print(f"Attempts remaining: {max_attempts - attempts}")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")
            attempts += 1
            print(f"Attempts remaining: {max_attempts - attempts}")

    print("Too many failed attempts. Account locked.") # prints this message when maximum attempt exceeded

if __name__ == "__main__":
    login_system()