import datetime


def is_valid_date(date_str: str) -> bool:
    """
    Check if the date is valid

    Args:
        date_str (str): The date to check

    Returns:
        bool: True if the date is valid, False otherwise
    """
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def is_valid_player_national_id(id_national: str) -> bool:
    """
    Check if the player national id is valid

    Args:
        id_national (str): The player national id to check

    Returns:
        bool: True if the player national id is valid, False otherwise
    """

    if len(id_national) != 7:
        return False
    if not id_national[:2].isalpha():
        return False
    if not id_national[2:].isdigit():
        return False
    return True
