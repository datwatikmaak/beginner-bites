import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    result = IS_EMOJI.findall(text)

    chars = [char for char in text]

    return [index for index in range(len(chars)) if chars[index] in result]
