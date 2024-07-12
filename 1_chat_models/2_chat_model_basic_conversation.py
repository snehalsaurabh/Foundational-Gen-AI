from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# Import ChatGemini instead of ChatOpenAI
from utils.gemini_langchain_integration import ChatGemini

# Load environment variables from .env
load_dotenv()

# Create a ChatGemini model instance, using the correct environment variable for the API key
model = ChatGemini(api_key=os.getenv("GOOGLE_API_KEY"))

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
