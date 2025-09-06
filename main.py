import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from functions.get_files_info import get_files_info
from call_function import available_functions,call_function





def main():
    print("hello from ai-agent!")

    load_dotenv()
    api_key=os.environ.get('GEMINI_API_KEY')

    # connecting to gemini api
    client = genai.Client(api_key=api_key)

    if  len(sys.argv)<2 or not sys.argv[1]:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)


    user_prompt=sys.argv[1]

    verbose = "--verbose" in sys.argv

    # list to remember context of the conversation
    messages = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(0,20):
        try:
            response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],
                                            system_instruction=system_prompt))
            
        except Exception as e:
            return(f"Error while connectint to clinet ,{e}")
    
        
       
    
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        
        if sys.argv[len(sys.argv)-1]== '--verbose':
            print("User prompt:",user_prompt)
            print("Prompt tokens:",response.usage_metadata.prompt_token_count)
            print("Response tokens:",response.usage_metadata.candidates_token_count)


        if response.function_calls:
            function_responses = []
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                resp = call_function(function_call_part)

                message = types.Content(
                    role="user",
                    parts=resp.parts
                )

                messages.append(message)

                if not resp.parts[0].function_response.response:
                    raise Exception("empty function call result")
                
                if verbose:
                    print(f"-> {resp.parts[0].function_response.response}")
                    function_responses.append(resp.parts[0])

         
            
            continue
        
        if response.text:
            print("Final Response")
            print(response.text)
            break

    


if __name__ == "__main__":
    main()
