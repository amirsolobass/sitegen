# AI Agent

An intelligent code assistant powered by Google's Gemini API, equipped with function calling capabilities to help with code generation, analysis, and automation tasks.

## Features

- AI Powered Code Generation - Leverages Google's Gemini API for intelligent code suggestions and generation
- Function Calling - Extended capabilities through dynamically callable functions
- Multi turn Conversations - Maintains context across multiple interactions
- Verbose Mode - Detailed output for debugging and understanding model responses
- File Operations - Can read, write, and analyze project files
- Content Generation - Automatically generate code and documentation

## Installation

1. Clone or download the project:
   ```bash
   cd aiagent
   ```

2. Ensure Python 3.8+ is installed

3. Install dependencies using pip or your preferred package manager:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using the included pyproject.toml:
   ```bash
   pip install .
   ```

4. Set up your environment:
   - Create a .env file or use apikey.env in the project root
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

Run the AI agent with a prompt:

```bash
python3 main.py "Your prompt here"
```

### Examples

- Generate Python code:
  ```bash
  python3 main.py "Write a function to calculate fibonacci numbers"
  ```

- Analyze code:
  ```bash
  python3 main.py "Review this code for best practices"
  ```

- Enable verbose output:
  ```bash
  python3 main.py "Your prompt" --verbose
  ```

## Project Structure

- main.py: Main entry point for the AI agent
- config.py: Configuration settings
- prompts.py: System prompts and prompt templates
- call_function.py: Function calling orchestration
- functions: Available functions the AI can call
  - generate_content.py: Generate new content
  - get_file_content.py: Read file contents
  - get_files_info.py: Get information about files
  - run_python_file.py: Execute Python files
  - write_file.py: Write or modify files
- calculator: Example calculator module

## Testing

Run the test suite:

```bash
python3 test_get_file_content.py
python3 test_get_files_info.py
python3 test_run_python_file.py
python3 test_write_file.py
```

## Development

The project uses available functions that the AI can call:
- Content generation
- File I/O operations
- Python code execution

Extend functionality by adding new functions in the functions/ directory.

## Requirements

- Python 3.8+
- Google Gemini API key
- Required Python packages (specified in pyproject.toml)

## Safety Notice

USE AT YOUR OWN RISK! This tool gives an AI model the ability to:
- Execute Python code
- Read and write files
- Generate content

Always review generated code and use in controlled environments. Never expose your API keys in version control.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.


**[Back to the Main Page](/)**