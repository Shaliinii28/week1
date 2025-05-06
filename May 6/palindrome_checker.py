'''
Name: Birashalynee Suthahar
Program: Palindrome Checker
'''

# function to check whether an input is palindrome or not
def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare characters from start and end
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False #not palindrome
        left += 1
        right -= 1
    
    return True #palindrome

def check_palindrome():
    # Get input from user
    user_input = input("Enter a string to check if it's a palindrome: ")
    
    # Check if palindrome and print result
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    check_palindrome()