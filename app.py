import chainlit as cl
import maritalk
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

url = "https://chat.maritaca.ai/api/chat/inference"


auth_header = {
    "authorization": f"Key {api_key}"
}

textos = []

model = maritalk.MariTalk(
    key=api_key,
    model=model
)

textos = []
response_data = {"answer": "Error"}

@cl.on_message
async def main(message: cl.Message, textos=textos, response_data=response_data):
    textos.append({"role": "user", "content": message.content})
    answer = model.generate(textos)['answer']
    textos.append({"role": "assistant", "content": response_data["answer"]})
    await cl.Message(
        content=f"{answer}",
    ).send()
