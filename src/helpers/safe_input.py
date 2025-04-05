from datetime import datetime
from src.helpers.colors import bcolors


def safe_input(
    prompt: str,
    type=str,
    min_value=None,
    max_value=None,
    allow_empty=False,
    date_format="%d/%m/%Y"
) -> any:
    """
    Safely get user input with validation
    """
    while True:
        try:
            user_input = input(prompt)

            if not user_input and allow_empty:
                return None

            if not user_input:
                print(f"{bcolors.FAIL}Ce champ est obligatoire.{bcolors.ENDC}")
                continue

            # Handle date conversion
            if type == datetime.date:
                try:
                    parsed_date = datetime.strptime(user_input, date_format)
                    return parsed_date.strftime(date_format)
                except ValueError:
                    print(f"{bcolors.FAIL}Format de date invalide. Utilisez le format {date_format}{bcolors.ENDC}")
                    continue

            # Handle integer conversion
            if type == int:
                try:
                    value = int(user_input)
                    if min_value is not None and value < min_value:
                        print(f"{bcolors.FAIL}La valeur doit être supérieure ou égale à {min_value}{bcolors.ENDC}")
                        continue
                    if max_value is not None and value > max_value:
                        print(f"{bcolors.FAIL}La valeur doit être inférieure ou égale à {max_value}{bcolors.ENDC}")
                        continue
                    return value
                except ValueError:
                    print(f"{bcolors.FAIL}Veuillez entrer un nombre entier valide.{bcolors.ENDC}")
                    continue

            return user_input

        except KeyboardInterrupt:
            print("\nOpération annulée.")
            return None
