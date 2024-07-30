import chainlit as cl
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("API_KEY_MARITACA")
model = os.getenv("MODEL_MARITACA")

textos = []

client = openai.OpenAI(
  api_key=api_key,
  base_url="https://chat.maritaca.ai/api",
)

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Olá, eu sou a Maritaca, sua assistente virtual. Como posso te ajudar?",
    ).send()

@cl.on_message
async def main(message: cl.Message):
    textos.append({"role": "user", "content": message.content})
    answer = client.chat.completions.create(
                model="sabia-3",
                messages=textos
            ).choices[0].message.content
    textos.append({"role": "assistant", "content": answer})
    await cl.Message(
        content=f"{answer}",
    ).send()
