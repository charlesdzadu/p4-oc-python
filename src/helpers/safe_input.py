from src.helpers.colors import bcolors


def safe_input(prompt: str, type: type = str, min_value=None, max_value=None, date_format="%Y-%m-%d", allow_empty=False) -> type:
    """
    Safe input function that validates user input based on the specified type and value constraints.
    
    Args:
        prompt: The prompt message to display to the user
        type: The expected type of the input (int, float, str, datetime.date, etc.)
        min_value: The minimum acceptable value (for int/float/date) or length (for str)
        max_value: The maximum acceptable value (for int/float/date) or length (for str)
        date_format: Format string for date parsing (default: YYYY-MM-DD)
        allow_empty: Whether to allow empty input (returns default if True)
    
    Returns:
        The validated input value of the specified type or None if escaped
    """
    import datetime
    
    while True:
        try:
            user_input = input(prompt)
            
            # Handle empty input
            if not user_input:
                if allow_empty:
                    return None
                else:
                    print("Erreur: Une entrée est requise.")
                    continue
            
            # Handle escape sequences
            if user_input.lower() in ['q', 'quit', 'exit', 'cancel', 'escape']:
                return None
                
            # Handle date types
            if type == datetime.date or type == datetime.datetime:
                try:
                    # Parse the date string
                    date_obj = datetime.datetime.strptime(user_input, date_format)
                    
                    # Convert to the specific date type requested
                    if type == datetime.date:
                        value = date_obj.date()
                    else:
                        value = date_obj
                    
                    # Check date constraints
                    if min_value is not None and value < min_value:
                        print(f"{bcolors.FAIL} Erreur: La date doit être le {min_value.strftime(date_format)} ou après.{bcolors.ENDC}")
                        continue
                        
                    if max_value is not None and value > max_value:
                        print(f"{bcolors.FAIL} Erreur: La date doit être le {max_value.strftime(date_format)} ou avant.{bcolors.ENDC}")
                        continue
                        
                    return user_input
                    
                except ValueError:
                    print(f"{bcolors.FAIL} Erreur: La date doit être valide dans le format {date_format}. Veuillez réessayer.{bcolors.ENDC}")
                    continue
            
            # Convert to the requested type
            if type == str:
                value = user_input
                
                # Check string length constraints
                if min_value is not None and len(value) < min_value:
                    print(f"{bcolors.FAIL} Erreur: La chaîne doit contenir au moins {min_value} caractères.{bcolors.ENDC}")
                    continue
                    
                if max_value is not None and len(value) > max_value:
                    print(f"{bcolors.FAIL} Erreur: La chaîne doit contenir au plus {max_value} caractères.{bcolors.ENDC}")
                    continue
                    
            else:
                # Handle numeric types
                value = type(user_input)
                
                # Check numeric constraints
                if min_value is not None and value < min_value:
                    print(f"{bcolors.FAIL} Erreur: La valeur doit être au moins {min_value}.{bcolors.ENDC}")
                    continue
                    
                if max_value is not None and value > max_value:
                    print(f"{bcolors.FAIL} Erreur: La valeur doit être au plus {max_value}.{bcolors.ENDC}")
                    continue
            
            return user_input
            
        except ValueError:
            print(f"{bcolors.FAIL} Erreur: La valeur doit être valide dans le format {type.__name__}. Veuillez réessayer.{bcolors.ENDC}")

