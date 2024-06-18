"""
This module provides functions for saving and loading LangChain documents to/from a JSONL file.

https://gist.github.com/dcbark01/59b8ad9f12f4cbecc791c3618bdde0b0
"""

import typing as t
import jsonlines
from langchain.schema import Document


def save_docs_to_jsonl(documents: t.Iterable[Document], file_path: str) -> None:
    """
    Save a collection of documents to a JSONL file.

    Args:
        documents (Iterable[Document]): The collection of documents to be saved.
        file_path (str): The path to the JSONL file.

    Returns:
        None
    """
    with jsonlines.open(file_path, mode="w") as writer:
        for doc in documents:
            writer.write(doc.dict())


def load_docs_from_jsonl(file_path) -> t.Iterable[Document]:
    """
    Load documents from a JSONL file.

    Args:
        file_path (str): The path to the JSONL file.

    Returns:
        Iterable[Document]: An iterable of Document objects.
    """
    documents = []
    with jsonlines.open(file_path, mode="r") as reader:
        for doc in reader:
            documents.append(Document(**doc))
    return documents
