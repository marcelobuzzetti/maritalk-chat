import chainlit as cl
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

textos = []

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    # ... more settings
}

client = AsyncOpenAI()

cl.instrument_openai()

@cl.on_message
async def on_message(message: cl.Message):
    textos.append({"role": "user", "content": message.content})
    response = await client.chat.completions.create(
        messages=textos,
        **settings
    )
    textos.append({"role": "system", "content": response.choices[0].message.content})
    await cl.Message(content=response.choices[0].message.content).send()