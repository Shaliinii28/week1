import re
from collections import Counter

def count_word_frequency(file_path):
    try:
        # Initialize an empty string to store text
        text = ""
        
        # Read the file in chunks to handle large files efficiently
        with open(file_path, 'r', encoding='utf-8') as file:
            for chunk in iter(lambda: file.read(8192), ''):
                text += chunk.lower()  # Convert to lowercase for consistency

        # Remove punctuation and split into words using regex
        words = re.findall(r'\b\w+\b', text)

        # Count frequency of each word using Counter
        word_counts = Counter(words)

        # Sort by frequency (most common first) and alphabetically for ties
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        # Print results
        print("Word Frequency Count:")
        for word, count in sorted_counts:
            print(f"{word}: {count}")

        return word_counts

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
    count_word_frequency(file_path)