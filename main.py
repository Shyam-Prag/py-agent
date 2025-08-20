import os
import sys 
from google import genai
from google.genai import types 
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():    
    print(sys.argv)
    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
    
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )
    
    if input_is_verbose():
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


def input_is_verbose() -> bool:
    if sys.argv[2] == "--verbose":
        return True 
    else:
        return False

if __name__ == "__main__":
    main()