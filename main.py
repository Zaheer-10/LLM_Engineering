import chainlit as cl
import os
import openai
from dotenv import load_dotenv, find_dotenv

api_key = os.environ.get("API_KEY")

# @cl.on_message
# async def main(message):
# await cl.Message(content=message).send()
#OUTPUT
# {
#     "id": "chatcmpl-87mOAOMWpui1Y8xiVl0HOS98B3NVy",
#     "object": "chat.completion",
#     "created": 1696864994,
#     "model": "gpt-3.5-turbo-0613",
#     "choices": [
#         {
#             "index": 0,
#             "message": {
#                 "role": "assistant",
#                 "content": "Hello! How can I assist you today?"
#             },
#             "finish_reason": "stop"
#         }
#     ],
#     "usage": {
#         "prompt_tokens": 17,
#         "completion_tokens": 9,
#         "total_tokens": 26
#     }
# }


@cl.on_message
async def main(message):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'assistant', 'content': 'You are a helpful assistant'},
            {'role': 'user', 'content': message}
        ],
        temperature=0.8

    )
    # await cl.Message(content=response).send()

    # await cl.Message(content=response['choices'][0]['message']['content']).send()
    await cl.Message(content=f"{response['choices'][0]['message']['content']}" , ).send()
    
    
# OUTPUT :  User

# 08:57:34 PM

# Hello how are you? what is the date and time

# Chatbot

# 08:57:37 PM

# Hello! I'm just a virtual assistant, so I don't experience emotions, but I'm here to help you.

# As for the date and time, it depends on your location. Could you please let me know where you are?