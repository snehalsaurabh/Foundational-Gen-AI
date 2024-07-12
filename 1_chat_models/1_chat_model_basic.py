# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
# Assuming ChatGemini is a class you have that can interact with Google Gemini
from your_gemini_integration import ChatGemini

# Load environment variables from .env
load_dotenv()

# Create a ChatGemini model instance
model = ChatGemini(api_key="YOUR_GOOGLE_API_KEY")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
