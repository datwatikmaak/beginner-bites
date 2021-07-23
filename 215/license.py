import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    # pattern = "^PB(-[A-Z0-9]{8}){4}$"
    # test_string = key
    result = re.match("^PB(-[A-Z0-9]{8}){4}$", key)

    return bool(result)
