import openai
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Set up the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)


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

        # Remove the backticks
        cleaned_code = code.replace("```python", "").replace("```", "").strip()

        # Print the generated code
        print("Generated Python Code:")
        print(cleaned_code)

        # Save the cleaned code to a file
        save_code_to_file(cleaned_code)

        return cleaned_code

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def save_code_to_file(code, filename="generatedcode.py"):
    """Save the generated Python code to a file."""
    try:
        with open(filename, "w") as f:
            f.write(code)
        print(f"Code has been written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    # Define your updated prompt
    prompt = (
        "Create a Python program that checks if a number is even. "
        "Do not write any explanations, just show me the code. "
        "The code should be saved to a new file called `generatedcode.py`."
        "Also include running unit tests with asserts that check the logic of"
        "the program. "
        "Make sure to also check interesting edge cases."
        "There should be at least 10 different unit tests."
    )

    # Get the Python code from ChatGPT and save it to a file
    get_python_code_from_chatgpt(prompt)
