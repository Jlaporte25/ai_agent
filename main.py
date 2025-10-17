import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

def main():
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
        system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")

        client = genai.Client(api_key=api_key)

        available_functions = types.Tool(
                funtion_declarations=[
                    schema_get_files_info,
                    ]
                )

        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
                )
        )       

        if len(sys.argv) > 2:
            if sys.argv[2] == "--verbose":
                print(f"User prompt: {user_prompt}")
                print(f"Response: {response.text}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        else:
            print(response.text)
    else:
        print("add prompt")
        sys.exit(1)

if __name__ == "__main__":
    main()
