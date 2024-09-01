"""
Script for housing the llm client

To test the client
"""

import os
from groq import Groq

from src.utils.dotenv import load_env_vars

class LLMClient():

    def __init__(self) -> None:
        load_env_vars()

        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )


    # TODO: Make this into a __call__
    def generate(self, user_query:str):

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Provide me a short workout of 3-4 sets. Each set consisting of 2-3 workouts. \
                                The workouts should all be centered around {user_query}",
                }
            ],
            model="llama3-8b-8192",
        )

        return chat_completion
    





