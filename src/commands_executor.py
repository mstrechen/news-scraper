import sys
import time

def run_commands_executor():
    while True:
        try:
            command = input()
            if command == "exit":
                print("Execution is interrupted by command")
                sys.exit()
        except EOFError:
            time.sleep(10)