from src.views.app_view import AppView
from src.helpers.signal_handler import setup_signal_handlers
from src.helpers.constants import LOGO_TOURNOI_ECHECS
from src.helpers.colors import bcolors


def main():
    # Setup signal handlers
    setup_signal_handlers()
    
    # Display welcome message
    print(LOGO_TOURNOI_ECHECS)
    print(f"\n{bcolors.OKBLUE}Bienvenue dans le gestionnaire de tournois d'échecs !{bcolors.ENDC}\n")
    
    # Start the application
    app_view = AppView()
    app_view.start()


if __name__ == "__main__":
    main()
