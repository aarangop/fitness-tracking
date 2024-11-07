import os
import yaml
import numpy as np
import pandas as pd
import re


def load_note(note_path: str) -> str:
    """
    Loads the content of a note file.
    Args:
      note_path (str): The path to the note file.
    Returns:
      str: The content of the note file.
    """
    try:
        with open(note_path, 'r') as f:
            note = f.read()
    except FileNotFoundError:
        note = ""

    return note


def parse_obsidian_metadata(note_path: str) -> dict:
    """
    Extracts metadata from an Obsidian note including arrays.
    Args:
      note_path (str): The path to the note file.
    Returns:
      dict: A dictionary containing the extracted metadata including arrays.
    """
    note = load_note(note_path)

    # Find metadata section between --- markers
    pattern = r'^---\n(.*?)\n---'
    match = re.search(pattern, note, re.DOTALL)

    if not match:
        return {}

    # Extract yaml content
    yaml_content = match.group(1)

    try:
        # Parse yaml content into dictionary
        metadata = yaml.safe_load(yaml_content)
        return metadata if metadata else {}
    except yaml.YAMLError:
        return {}
