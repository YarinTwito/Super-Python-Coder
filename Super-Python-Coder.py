# Super-Python-Coder.py
import random
import subprocess
import openai
import os
import time
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
        start_time = time.time()  # Measure time before running the code
        subprocess.run(["python3", filename], check=True)
        end_time = time.time()  # Measure time after running the code
        execution_time = (end_time - start_time) * 1000
        print(f"Code ran in {execution_time:.2f} milliseconds")
        return execution_time
    except subprocess.CalledProcessError as e:
        print(f"Error running generated code! Error: {e}")
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
        "\n Create a Python program based on the above description. "
        "The program should be clear, well-documented, and follow PEP 8 and "
        "Flake8 guidelines. Don't write any explanations.  "
        "Also include running unit tests with asserts that check the logic of"
        "the program. Make sure to also check edge cases."
    )
    with alive_bar(5, title="Code Generation Progress") as bar:  # 5 attempts
        for attempt in range(5):
            print(f"\nAttempt {attempt + 1} to generate and run the code...")

            code = get_python_code_from_chatgpt(prompt)
            if not code:
                print("Failed to generate code from OpenAI. Exiting.")
                break

            execution_time_before = save_code_to_file(code)
            if execution_time_before is None:
                print("Error running generated code! Trying again...")
            else:
                print("Code created successfully!")
                bar(5)

                # Request optimized code from OpenAI
                print("\nRequesting optimized code...")
                optimized_prompt = prompt + (
                    "\nImprove the performance of the code to run faster."
                )
                optimized_code = get_python_code_from_chatgpt(optimized_prompt)

                if optimized_code:
                    print("\nOptimized code generated. Saving to file...")
                    execution_time_after = save_code_to_file(optimized_code)

                    if execution_time_after is None:
                        print("Error running optimized code!")
                    else:
                        # Compare execution times
                        if execution_time_after < execution_time_before:
                            print(
                                f"Code running time optimized! It now runs in "
                                f"{execution_time_after:.2f} milliseconds, "
                                f"while before it was "
                                f"{execution_time_before:.2f} milliseconds"
                            )
                        else:
                            print("The optimized code didn't improve the "
                                  "performance.")
                break

            # Update progress bar after each attempt
            bar()

        else:
            print("Code generation FAILED after 5 attempts.")


if __name__ == "__main__":
    main()
