
import openai
from dotenv import load_dotenv
import os


class ChatGPTPRediction:

    def __init__(self, url: str) -> None:

        self.url: str = url

    def run(self, dependencies: list) -> dict:

        load_dotenv()
        api_key: str = os.getenv('openAI_API_KEY')        
        filtered_text: str = dependencies[0]['parsed_pages'][self.url]
