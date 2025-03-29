import random
import string


def generate_id(size: int = 20):
    """
    Generate a random id
    """
    tmp_id = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return tmp_id.lower()
