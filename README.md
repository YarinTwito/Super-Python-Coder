# Super-Python-Coder

Super-Python-Coder is a Python-based application designed to generate Python code using OpenAI's GPT models. The project integrates OpenAI's API to create programs based on user-provided prompts, improve code quality by running lint checks, and even test execution performance. With a fun and interactive interface, it’s the perfect tool for experimenting with AI-generated code and improving coding skills.

## Features
- **Code Generation**: Generate Python programs based on user-provided or random prompts.
- **Lint Checks**: Automatically run `pylint` on generated code to ensure it adheres to PEP 8 and other best practices.
- **Error Fixing Loop**: Iteratively improve the generated code by addressing linting errors up to 3 attempts.
- **Unit Tests**: Generated code includes unit tests to verify logic and edge cases.
- **Execution Metrics**: Measure execution time for generated programs.

## Installation

### Prerequisites
- Python 3.8 or higher
- A virtual environment (recommended)
- OpenAI API key

### Clone the Repository
```bash
git clone https://github.com/YarinTwito/Super-Python-Coder.git
cd Super-Python-Coder
```

### Set Up the Environment
1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:
   Create a `.env` file in the project directory and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage
1. Run the program:
   ```bash
   python super_python_coder.py
   ```

2. Follow the prompts:
   - Provide a custom program idea.
   - Or press Enter to let the app randomly select a program idea.

3. The generated code will:
   - Be saved to `best_version.py`.
   - Run unit tests.
   - Perform lint checks and fix issues if needed.

## File Structure
- `Super-Python-Coder.py`: Main script for the application.
- `best_version.py`: The final version of the generated code.
- `Requested-code.py`: Backup of generated code from the last run.
- `.env`: Environment variables file (contains API key).
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## Example Workflow
1. **Prompt**: 
   Provide the following prompt:
   ```plaintext
   A program that checks if a number is a palindrome.
   ```

2. **Generated Output**: 
   A Python script that checks for palindromes, with unit tests to handle edge cases.

3. **Lint Checks**: 
   The script automatically runs `pylint` and resolves any linting issues iteratively.

4. **Final Output**:
   A well-documented, optimized Python script is saved to `best_version.py`.

## Contributing
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or feedback, reach out to:
- **Author**: Yarin Twito
- **GitHub**: [YarinTwito](https://github.com/YarinTwito)
