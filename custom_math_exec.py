import math

from globals import *

class CustomExec:
    def squareRoot(self, num: int | float) -> int:
        return math.sqrt(num)
    
    def __init__(self, customCode: str) -> None:
        self.customCode: str = customCode
        
        self.commandMap = {
            "sr": self.squareRoot
        }
    
    def get_return(self) -> any:
        commands: list[str] = self.customCode.split(" ")
        
        specialCommand = commands[0]
        regularCommands = commands[1:]
        
        exec_namespace = {}
        exec(f"x = {"".join(regularCommands)}", exec_namespace)
        
        parsedExpressionValue: int = exec_namespace["x"]
        
        return self.commandMap[specialCommand](parsedExpressionValue)