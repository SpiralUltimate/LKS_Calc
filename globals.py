from enum import Enum


OPERATORS = ["+", "-", "*", "/", "^"]

CUSTOM_COMMANDS = ["sr"]

class TerminalModes(Enum):
    MATH = 0
    WINDOWS = 1

DEFAULT_MODE: TerminalModes = TerminalModes.MATH