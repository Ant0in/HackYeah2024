
import openai
from dotenv import load_dotenv
import os


class ChatGPTPrediction:

    def __init__(self, url: str) -> None:

        self.url: str = url

    def run(self, dependencies: list) -> dict:

        load_dotenv()
        api_key: str = os.getenv('openAI_API_KEY')        
        
        if not api_key:
            print("API key not found. Please set the openAI_API_KEY in the .env file.")
            return dict()
        
        openai.api_key = api_key

        filtered_text: str = dependencies[0]['parsed_pages'][self.url]
        themes: str = list(dependencies[1]['themes'])

        prompt: str = f"Analyze the main theme and content of this webpage, then assess whether \
            the site appears fraudulent or secure. Based on factors such as the presence of \
            legitimate information, offers that seem too good to be true, grammar errors, \
            legal disclaimers, or dubious practices, provide a confidence score between \
            0 (completely fraudulent) and 100 (completely secure). Respond with only a numeric score. \
            here are the page link : {self.url}, the themes : {themes} and the page content : {filtered_text}."

        try:
            
            completion = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )
            generated_text = completion.choices[0].message.content.strip()
            
            return {
                'score': float(generated_text) / 100
            }

        except Exception as e:
            print(f"Error calling OpenAI API: {str(e)}")
            return {
                'error': str(e)
            }