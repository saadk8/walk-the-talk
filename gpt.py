from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
import random
import time
import logging

load_dotenv()
client = OpenAI()

def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 5,
    errors: tuple = (openai.RateLimitError,),
):
    """Retry a function with exponential backoff."""

    def wrapper(*args, **kwargs):
        # Initialize variables
        num_retries = 0
        delay = initial_delay

        # Loop until a successful response or max_retries is hit or an exception is raised
        while True:
            try:
                return func(*args, **kwargs)

            # Retry on specified errors
            except errors as e:
                # Increment retries
                num_retries += 1

                # Check if max retries has been reached
                if num_retries > max_retries:
                    raise Exception(
                        f"Maximum number of retries ({max_retries}) exceeded."
                    )

                # Increment the delay
                delay *= exponential_base * (1 + jitter * random.random())

                # Sleep for the delay
                time.sleep(delay)

            # Raise exceptions for any errors not specified
            except Exception as e:
                raise e

    return wrapper


@retry_with_exponential_backoff
def get_AI_response(prompt, model="gpt-4-1106-preview", temperature=0.2, system_message="", response_format=None):
    try:
        create_params = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": "Business Details: \n" + prompt},
            ],
            "temperature": temperature,
        }
        if response_format:
            create_params["response_format"] = response_format

        response = client.chat.completions.create(**create_params)
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error getting AI response: {e}", exc_info=True)
        return None