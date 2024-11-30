# Super-Python-Coder.py
import random
import subprocess
import openai
import os
from dotenv import load_dotenv
from alive_progress import alive_bar

# Load the environment variables from .env file
load_dotenv()

# Set up the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Constant list of program ideas
PROGRAMS_LIST = [
    # First program idea
    '''Given two strings str1 and str2, prints all interleavings of the given
two strings. You may assume that all characters in both strings are
different.
Input: str1 = "AB", str2 = "CD"
Output:
ABCD
ACBD
ACDB
CABD
CADB
CDAB
Input: str1 = "AB", str2 = "C"
Output:
ABC
ACB
CAB ''',


    # Second program idea
    "A program that checks if a number is a palindrome",

    # Third program idea
    "A program that finds the kth smallest element in a given "
    "binary search tree.",

    # Fourth program idea
    ''' Given an m x n matrix mat, return an array of all the elements of the
    array in a diagonal order.
    Example 1:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
    Example 2:
    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]''',

    # Fifth program idea
    ''' Given an integer number n, return the difference between the product
    of its digits and the sum of its digits.
    Example 1:
    Input: n = 234
    Output: 15
    Explanation:
    Product of digits = 2 * 3 * 4 = 24
    Sum of digits = 2 + 3 + 4 = 9
    Result = 24 - 9 = 15
    Example 2:
    Input: n = 4421
    Output: 21
    Explanation:
    Product of digits = 4 * 4 * 2 * 1 = 32
    Sum of digits = 4 + 4 + 2 + 1 = 11
    Result = 32 - 11 = 21
    Constraints:
    1 <= n <= 10^5 ''',
]


def get_python_code_from_chatgpt(prompt):
    try:
        # Requesting chat completion with the correct client structure
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o-mini",  # Use the gpt-4-mini model
        )

        # Extract the generated code from the response
        code = response.choices[0].message.content.strip()
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()

        return code
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return None


def save_code_to_file(code, filename="Requsted-code.py"):
    """Save the generated Python code to a file."""
    with open(filename, "w") as f:
        f.write(f"# {filename}\n")
        f.write(code)
    try:
        subprocess.run(["python3", filename], check=True)
        print("Code creation completed successfully!")
        subprocess.call(["open", filename])  # Open the file on macOS
        return None
    except subprocess.CalledProcessError as e:
        return e

    return None


def main():
    print("I’m Super Python Coder. Tell me, which program would you like me "
          "to code for you?")
    print("If you don't have an idea, just press enter and "
          "I will choose a random program to code.")
    # Get user input
    user_input = input("Your program idea: ").strip()

    if user_input == "":
        # Select a random program from the list
        chosen_program = random.choice(PROGRAMS_LIST)
        print("\nYou didn't choose a program, so here's a random one:\n")
        prompt = chosen_program
    else:
        print("\nGreat! Here's the program idea you provided:\n")
        prompt = user_input

    # Add unit test requirements to the prompt
    prompt += (
        "\n Create a Python program for the above. "
        "Include unit tests with 'asserts' to validate the functionality. "
        "Ensure unit tests are consistent with the program logic. "
        "Include at least 10 tests, covering edge cases, valid inputs. "
        "Provide only the Python code, without explanations."
    )

    with alive_bar(5, title="Code Generation Progress") as bar:  # 5 attempts
        for attempt in range(5):
            print(f"\nAttempt {attempt + 1} to generate and run the code...")

            # Generate the code using GPT-4
            code = get_python_code_from_chatgpt(prompt)
            if not code:
                print("Failed to generate code from OpenAI. Exiting.")
                break

            error = save_code_to_file(code)

            if error:
                print(f"Error running generated code! Error: {error}. "
                      "Trying again...")
            else:
                print("Code created successfully!")
                if not error:  # Check for success after saving
                    print(f"Code generation successful on attempt "
                          f"{attempt + 1}!")
                    break
            # Update the progress bar after each attempt
            bar()

        else:
            print("Code generation FAILED after 5 attempts.")


if __name__ == "__main__":
    main()
