import chainlit as cl
import maritalk
from dotenv import load_dotenv
import os
# from openai import AsyncOpenAI

# client = AsyncOpenAI()

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("API_KEY_MARITACA")
model = os.getenv("MODEL_MARITACA")

textos = []

model = maritalk.MariTalk(
    key=api_key,
    model=model
)

@cl.on_message
async def main(message: cl.Message):
    textos.append({"role": "user", "content": message.content})
    answer = model.generate(textos)['answer']
    textos.append({"role": "assistant", "content": answer})
    await cl.Message(
        content=f"{answer}",
    ).send()
