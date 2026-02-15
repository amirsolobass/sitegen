# BookBot

BookBot is a command-line tool for analyzing text files. It provides detailed statistics about words and character frequencies in any book or text document.

## Features

- **Word Count**: Get the total number of words in your document
- **Character Frequency Analysis**: See detailed counts of every character
- **Simple CLI**: Easy-to-use command-line interface
- **Formatted Output**: Clean, readable output with organized statistics
- **Any Text File**: Works with any txt file or text based document

## Installation

1. Clone or download the project:
   ```bash
   cd bookbot
   ```

2. Ensure Python 3.8+ is installed

3. No external dependencies required! Just standard Python libraries.

## Usage

Analyze any text file with a simple command:

```
python3 main.py path/to/your/book.txt
```

### Examples

- Analyze Frankenstein:
  ```bash
  python3 main.py books/frankenstein.txt
  ```

- Analyze Pride and Prejudice:
  ```bash
  python3 main.py books/prideandprejudice.txt
  ```

- Analyze Moby Dick:
  ```bash
  python3 main.py books/mobydick.txt
  ```

### Output Example

```
============ BOOKBOT ============
Analyzing book at: books/frankenstein.txt
=================================
Found 73115 total words
--------- Character Count -------
a: 5231
b: 1298
c: 2456
...
============= END ===============
```

## Project Structure

- main.py - Main entry point, handles file reading and output formatting
- stats.py - Core statistics functions
  - count words function - Counts total words
  - count chars function - Counts character frequencies
  - sort list function - Sorts results for display
- books folder - Sample text files for analysis
  - frankenstein.txt
  - mobydick.txt
  - prideandprejudice.txt

## How It Works

1. Read the specified text file
2. Count total words by splitting on whitespace
3. Count frequency of each character using case insensitive comparison
4. Sort results by frequency (highest to lowest)
5. Display formatted results

## Requirements

- Python 3.6+
- A text file to analyze

## About

BookBot is my first Boot.dev project. It demonstrates foundational Python skills including file input output, data processing, and command line interface development.

## Contributing

Feel free to fork and enhance! Possible improvements:
- Sentence and paragraph counting
- Average word length
- Most common words
- Reading time estimates

**[Back to the Main Page](/docs/sitegen/index.md)**
