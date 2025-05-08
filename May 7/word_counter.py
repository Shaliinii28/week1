import re

def count_total_words(file_path):
    try:
        # Initialize an empty string to store text
        text = ""
        
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            for chunk in iter(lambda: file.read(8192), ''):
                text += chunk.lower()  # Convert to lowercase

        # Remove punctuation and split into words using regex
        words = re.findall(r'\b\w+\b', text)

        # Count total number of words
        total_words = len(words)

        # Print result
        print(f"Total number of words: {total_words}")

        return total_words

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except MemoryError:
        print("Error: File is too large to process with available memory.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None

if __name__ == "__main__":
    # Prompt user for file path
    file_path = input("Enter the path to the text file: ")
    count_total_words(file_path)