import os
import sys
from colorama import Fore

from globals import *
from custom_math_exec import CustomExec

class Application:
    def __init__(self) -> None:
        self.currentMode = DEFAULT_MODE
    
    def executeWindowsCommand(self, command: str):
        try:
            os.system(command)
        except Exception as error:
            # Makes the error red.
            print(Fore.RED)
            print(error)
            # Resets the terminal color once the error message is finished.
            print(Fore.RESET)
    
    def run(self):
        while True:
            containsCommand = False
            userInput: str = input("<< ")
            
            # Allows our user to execute windows functions in math mode.
            if userInput.startswith("wx") and self.currentMode == TerminalModes.MATH:
                userInput = userInput.replace("wx", "")
                self.executeWindowsCommand(userInput)
                continue
            
            # Switches mode to windows mode if not already in windows mode.
            # Windows mode allows for execution of bash commands in our terminal.
            if userInput == "w" and self.currentMode != TerminalModes.WINDOWS:
                os.system(userInput.replace("w", ""))
                self.currentMode = TerminalModes.WINDOWS
                
                # Tells our user Windows Mode is activated.
                print("Windows Mode Activated!")
                
                continue
                
            # Switching back to math mode if we are in windows mode.
            if userInput == "m" and self.currentMode != TerminalModes.MATH:
                os.system(userInput.replace("m", ""))
                self.currentMode = TerminalModes.MATH
                
                # Tells our user Math Mode is activated.
                print("Math Mode Activated!")
                
                continue
            
            # This is the main bulk of our program.
            # This is what allows the user to do math stuff.
            
            if self.currentMode == TerminalModes.WINDOWS:
                self.executeWindowsCommand(userInput)
            
            elif self.currentMode == TerminalModes.MATH:
                try:
                    for command in CUSTOM_COMMANDS:
                        if command in userInput:
                            containsCommand = True
                    
                    if not containsCommand:
                        namespace = {}
                        exec(f"x = {userInput}", namespace)
                        print(namespace["x"])
                    else:
                        print(CustomExec(userInput).get_return())    
                except Exception as e:
                    print(f"Error: {e}")
                    continue