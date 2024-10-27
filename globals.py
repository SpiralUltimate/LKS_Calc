from enum import Enum
from colorama import Fore
from custom_math_exec import CustomExec


OPERATORS = ["+", "-", "*", "/", "^"]

DEBUG = True

def log(*args):
    """
    log() is a version of the print function specifically meant for 
    debugging
    """
    print(Fore.GREEN)
    print("DEBUG: ", *args)
    print(Fore.RESET)

# A list of all the custom math commands
# Retrieves commands from our customExec class
customMathCommands: list[str] = [key for key in CustomExec("").commandMap.keys()]

class TerminalModes(Enum):
    MATH = 0
    WINDOWS = 1

class ModeKeys(Enum):
    MATH_KEY = "m"
    WINDOWS_KEY = "w"

class SpecialKeys(Enum):
    WINDOWS_HYBRID_EXEC_KEY = "wx"

DEFAULT_MODE: TerminalModes = TerminalModes.MATH