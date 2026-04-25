import random
import string


def generate_password(length: int, use_digits: bool, use_special: bool, use_uppercase:bool) -> str:
    characters = string.ascii_lowercase  # всегда есть строчные буквы

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not any([use_digits, use_special, use_uppercase]):
        characters = string.ascii_lowercase

    return ''.join(random.choice(characters) for _ in range(length))