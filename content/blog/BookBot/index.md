# bookbot
Because it's so simple, I have no issue with sharing the source code right here on this page! This way you'll know I'm the real deal.
```
import sys
from stats import count_words, count_chars, sort_list

def get_book_text(file_path):
    with open(file_path) as file: # Open the book file
        book_text = file.read() # Read the entire content
        return book_text


def main():
    if len(sys.argv) != 2: # Check if book path is provided
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] # Get book path from command line argument
    book_text = get_book_text(book_path) # Get book text
    count = count_words(book_text) # Count words
    char_counts = count_chars(book_text) # Count characters
    char_counts = sort_list(char_counts) # Sort character counts
    print("============ BOOKBOT ============")
    print(f"Analyzing book at: {book_path}")
    print("=================================")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, count in char_counts: # Print each character and its count as a list
        print(f"{char}: {count}")
    print("============= END ===============")
    
main()
```
Also, I made this as my first [Boot.dev](https://www.boot.dev) project, so I can't take all the credit. Please don't sue me for showing the solution for an entire course.
That's all.

[< Back Home](/)
