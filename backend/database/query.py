"""Retrieve queries for usage in the db"""

import os
from pathlib import Path

from loguru import logger

logger = logger.opt(colors=True)


def create_file_content_dict(folder_path: Path) -> dict:
    """Creates a dictionary with filenames as keys and
    their contents as values."""
    file_content_dict = {}

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            with open(file_path, "r", encoding="UTF-8") as f:
                contents = f.read()
            file_content_dict[filename.split(".")[0]] = contents

    return file_content_dict


PATH = str(Path(__file__).parent / "queries/")
QUERIES = create_file_content_dict(PATH)

logger.trace("Got queries: <w>{}</>", QUERIES)
