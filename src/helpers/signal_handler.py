import signal
import sys
from src.helpers.colors import bcolors


def handle_ctrl_c(signum, frame):
    """
    Handle the CTRL+C signal gracefully
    """
    print(f"\n\n{bcolors.WARNING}Programme arrêté par l'utilisateur.{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}Au revoir ! 👋{bcolors.ENDC}\n")
    sys.exit(0)


def setup_signal_handlers():
    """
    Setup signal handlers for the program

    """
    # SIGINT for Signal Interrupt (Ctrl+C)
    signal.signal(signal.SIGINT, handle_ctrl_c)
