def count_words(book_text):
    words = book_text.split() # Split words
    count = len(words) # Count words
    return count

def count_chars(book_text):
    chars = {}  # Dictionary to hold character counts
    for char in book_text:  # Iterate through each character
        if char.isalpha(): # Check if character is a letter
            char = char.lower() # Convert to lowercase
            if char in chars: # If character already in dictionary, increment count
                chars[char] += 1 
            else: # If character not in dictionary, initialize count to 1
                chars[char] = 1
    return chars

def sort_list(chars):
    # Sort characters by frequency in descending order
    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars