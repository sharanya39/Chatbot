import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Groq Chat model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="mixtral-8x7b-32768"  # You can also use "llama3-8b" or "llama3-70b"
)

# Create a Langchain prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{user_input}")
])

# Function to get response from LLM
def get_chatbot_response(user_input):
    chain = prompt | llm
    response = chain.invoke({"user_input": user_input})
    return response.content
