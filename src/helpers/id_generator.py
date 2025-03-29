import random
import string


def generate_id(size: int = 10):
    """
    Generate a random id
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))
