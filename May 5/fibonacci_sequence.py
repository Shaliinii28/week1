'''
Name: Birashalynee Suthahar
Program: Build fibonacci series of n numbers
'''

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def print_fibonacci():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        
        if n <= 0:
            print("Please enter a positive number.")
            return
            
        fib_sequence = fibonacci(n)
        print(f"Fibonacci sequence up to {n} terms:")
        print(" ".join(map(str, fib_sequence)))
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    print_fibonacci()