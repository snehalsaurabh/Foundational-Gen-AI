# your_gemini_integration.py
import os
from dotenv import load_dotenv
from google.cloud import gemini
from langchain import LLMChain, PromptTemplate

class ChatGemini:
    def __init__(self, api_key=None, config_path=".env"):
        load_dotenv(config_path)
        self.api_key = api_key or os.getenv("YOUR_GOOGLE_API_KEY")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.client = gemini.Client()

    def _gemini_call(self, prompt):
        response = self.client.generate(prompt)
        return response.choices[0].text

    def create_chain(self, template_str, input_variables):
        prompt_template = PromptTemplate(input_variables=input_variables, template=template_str)
        return LLMChain(llm=self._gemini_call, prompt_template=prompt_template)

    def invoke(self, message):
        template_str = "{message}"
        input_variables = ["message"]
        chain = self.create_chain(template_str, input_variables)
        return chain.run({"message": message})
