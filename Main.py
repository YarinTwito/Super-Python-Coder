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

        # Clean up the markdown formatting (remove the backticks)
        cleaned_code = code.replace("```python", "").replace("```", "").strip()

        # Print only the generated Python code
        print("Generated Python Code:")
        print(cleaned_code)

        return cleaned_code

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Define your prompt
    prompt = (
        "Create a python program that checks if a number is prime. "
        "Do not write any explanations, just show me the code itself."
    )

    # Get the Python code from ChatGPT
    get_python_code_from_chatgpt(prompt)
