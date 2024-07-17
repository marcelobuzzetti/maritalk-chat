import chainlit as cl
import maritalk
from dotenv import load_dotenv
import os
import markdown2

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

model = maritalk.MariTalk(
    key=api_key,
    model=model  # No momento, suportamos os modelos sabia-3, sabia-2-medium e sabia-2-small
)


@cl.on_message
async def main(message: cl.Message):
    response = model.generate(message.content)
    answer = response["answer"]
    # html = markdown2.markdown(answer) 
    # return answer
    # return jsonify({'resposta': html}), 200
    await cl.Message(
        content=f"Received: {answer}",
    ).send()