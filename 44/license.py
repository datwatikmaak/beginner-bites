import string
import secrets


def gen_key(parts=4, chars_per_part=8):
    chars = string.ascii_uppercase + string.digits

    license_key = ""
    for i in range(parts):
        if i < parts - 1:
            license_key += f"{''.join(secrets.choice(chars) for i in range(chars_per_part))}-"
        else:
            license_key += f"{''.join(secrets.choice(chars) for i in range(chars_per_part))}"

    return license_key


gen_key()
