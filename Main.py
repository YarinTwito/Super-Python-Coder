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

        print(cleaned_code)
        print()
    
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
        print()
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    # Define your prompt
    prompt = (
        "Create a python program that checks if a number is prime. "
        "Do not write any explanations, just show me the code itself."
    )

    # Get the Python code from ChatGPT and save it to a file
    get_python_code_from_chatgpt(prompt)
