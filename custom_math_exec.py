import math

from globals import *

class CustomExec:
    def squareRoot(self, num: int | float) -> int:
        return math.sqrt(num)
    
    def square(self, num: int | float) -> int:
        return num * num
    
    def __init__(self, customCode: str) -> None:
        self.customCode: str = customCode
        
        # A simple dictionary containing all of our math custom commands.
        # Every function in this dictionary must return a number and-
        # Each function must take in a number value (int, float, etc.)
        self.commandMap = {
            "sr": self.squareRoot,
            "s": self.square
        }
    
    def get_return(self) -> any:
        commands: list[str] = self.customCode.split(" ")
        
        specialCommand = commands[0]
        regularCommands = commands[1:]
        
        exec_namespace = {}
        exec(f"x = {"".join(regularCommands)}", exec_namespace)
        
        parsedExpressionValue: int = exec_namespace["x"]
        
        try:
            return self.commandMap[specialCommand](parsedExpressionValue)
        except Exception as error:
            print(f"Error trying to execute {specialCommand} function:")
            print(error)