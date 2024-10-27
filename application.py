import os
import sys
from colorama import Fore

from globals import *
from custom_math_exec import CustomExec

class Application:
    def __init__(self) -> None:
        self.currentMode = DEFAULT_MODE
        
    def handleMathMode(self, userInput: str):
        try:
            for command in customMathCommands:
                if command in userInput:
                    self.containsCommand = True
                    
            if not self.containsCommand:
                namespace = {}
                exec(f"x = {userInput}", namespace)
                print(namespace["x"])
            else:
                print(CustomExec(userInput).get_return())    
        except Exception as e:
            print(f"Error: {e}")
            
            if DEBUG:
                log(f'Check if you added the "{userInput.split(" ")[0]}" ' + 
                      'command to your CUSTOM_MATH_COMMANDS list and also updated ' +
                      'your command map.'
                      )
    
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
            self.containsCommand = False
            userInput: str = input("<< ")
            
            # Allows our user to execute windows functions in math mode.
            if userInput.startswith(SpecialKeys.WINDOWS_HYBRID_EXEC_KEY.value) and self.currentMode == TerminalModes.MATH:
                userInput = userInput.replace(SpecialKeys.WINDOWS_HYBRID_EXEC_KEY.value, "")
                self.executeWindowsCommand(userInput)
                continue
            
            # Switches mode to windows mode if not already in windows mode.
            # Windows mode allows for execution of bash commands in our terminal.
            if userInput == ModeKeys.WINDOWS_KEY.value and self.currentMode != TerminalModes.WINDOWS:
                os.system(userInput.replace(ModeKeys.WINDOWS_KEY.value, ""))
                self.currentMode = TerminalModes.WINDOWS
                
                # Tells our user Windows Mode is activated.
                print(Fore.GREEN)
                print("Windows Mode Activated!")
                print(Fore.RESET)
                
                continue
                
            # Switching back to math mode if we are in windows mode.
            if userInput == ModeKeys.MATH_KEY.value and self.currentMode != TerminalModes.MATH:
                os.system(userInput.replace(ModeKeys.WINDOWS_KEY.value, ""))
                self.currentMode = TerminalModes.MATH
                
                # Tells our user Math Mode is activated.
                print(Fore.GREEN)
                print("Math Mode Activated!")
                print(Fore.RESET)
                
                continue
            
            # This is the main bulk of our program.
            # This is what allows the user to do math stuff.
            
            if self.currentMode == TerminalModes.WINDOWS:
                self.executeWindowsCommand(userInput)
                continue
            
            elif self.currentMode == TerminalModes.MATH:
                self.handleMathMode(userInput)
                continue