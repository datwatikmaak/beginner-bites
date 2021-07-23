PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new_text = ""
    for char in text:
        if char in PYBITES.upper() and char.isupper():
            new_text += char.lower()
        elif char in PYBITES.lower() and char.islower():
            new_text += char.upper()
        else:
            new_text += char

    return new_text
