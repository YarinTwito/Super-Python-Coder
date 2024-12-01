# Super-Python-Coder.py
import random
import subprocess
import openai
import os
import time
from dotenv import load_dotenv
from colorama import Fore, Style, init
from tqdm import tqdm
init(autoreset=True)

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
    Example 1:
    Input: str1 = "AB", str2 = "CD"
    Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

    Example 2:
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
    matrix in diagonal order. Ensure the function handles edge cases, such as
    when the matrix is empty or has only one row or column.
    Example 1:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]

    Example 2:
    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4] '''

    # Fifth program idea
    ''' Given two strings s and goal, return true if and only if s can become
    goal after some number of shifts on s.
    A shift on s consists of moving the leftmost character of s to the
    rightmost position.
    For example, if s = "abcde", then it will be "bcdea" after one shift.
    Example 1:
    Input: s = "abcde", goal = "cdeab"
    Output: true
    Example 2:
    Input: s = "abcde", goal = "abced"
    Output: false
    Constraints:
    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.''',
]

def get_python_code_from_chatgpt(prompt):
    try:
        # Requesting chat completion with the correct client structure
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o-mini",
        )

        # Extract the generated code from the response
        code = response.choices[0].message.content.strip()
        if "python" in code:
            code = code.split("python")[1].split("")[0].strip()
        elif "" in code:
            code = code.split("")[1].split("")[0].strip()

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
        start_time = time.time()  # Measure time before running the code
        subprocess.run(["python3", filename], check=True)
        end_time = time.time()  # Measure time after running the code
        execution_time = (end_time - start_time) * 1000
        print(f"Code ran in {execution_time:.2f} milliseconds")
        return execution_time
    except subprocess.CalledProcessError as e:
        print(f"Error running generated code! Error: {e}")
        return None

def run_lint_check(filename):
    """Run pylint on the given file and return the result."""
    try:
        result = subprocess.run(
            ["pylint", filename],
            capture_output=True,
            text=True,
        )
        return result.stdout, result.returncode
    except Exception as e:
        print(f"{Fore.RED}Error running pylint: {e}")
        return "", 1

def main():
    print(f"{Fore.GREEN}I’m Super Python Coder. Tell me, which program would you like me "
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
        "\n Create a Python program based on the above description. "
        "The program should be clear, well-documented, and follow PEP 8 and "
        "Flake8 guidelines. Don't write any explanations.  "
        "Also include running unit tests with asserts that check the logic of"
        "the program. Make sure to also check edge cases."
    )
    with tqdm(total=3, desc="Lint Fixing Progress") as progress_bar:
        for attempt in range(3):
            print(f"{Fore.CYAN}Attempt {attempt + 1} to generate and lint the code...")

            code = get_python_code_from_chatgpt(prompt)
            if not code:
                print(f"{Fore.RED}Failed to generate code from OpenAI. Exiting.")
                break

            # Save the code and run lint check
            filename = "best_version.py"
            save_code_to_file(code, filename)
            print(f"{Fore.GREEN}Code saved to {filename}. Running lint check...")

            lint_output, lint_status = run_lint_check(filename)

            if lint_status == 0:
                print(f"{Fore.GREEN}Amazing. No lint errors/warnings!")
                break
            else:
                print(f"{Fore.YELLOW}Lint warnings/errors detected:\n{lint_output}")
                prompt = (
                    f"Fix the following code to resolve linting issues:\n{code}\n"
                    f"Lint output:\n{lint_output}"
                )
                progress_bar.update(1)
        else:
            print(f"{Fore.RED}There are still lint errors/warnings after 3 attempts.")


if __name__ == "__main__":
    main() 
