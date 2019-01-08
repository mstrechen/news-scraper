import sys

def run_commands_executor():
    while True:
        command = input()
        if command == "exit":
            print("Execution is interrupted by command")
            sys.exit()
