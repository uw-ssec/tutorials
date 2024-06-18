"""
This module contains functions for parsing llama cpp responses.
"""


def parse_chat_completion_response(generated_response: dict) -> str:
    """
    Parses the generated response from llama cpp python create_chat_completion API and returns the message.

    Parameters:
    - generated_response (dict): The generated response from create_chat_completion API.

    Returns:
    - str: The message extracted from the generated response.
    """
    return generated_response["choices"][0]["message"]


def parse_text_generation_response(generated_response: dict) -> str:
    """
    Parses the generated response from llama cpp python text generation API and returns the message.

    Parameters:
    - generated_response (dict): The generated response from the llama cpp python text generation API.

    Returns:
    - str: The generated text.

    """
    return generated_response["choices"][0]["text"]
