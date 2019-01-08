#!/bin/python3
"""
    Main script
"""

import threading

from http_server import run_http_server
from commands_executor import run_commands_executor

if __name__ == "__main__":
    try:
        import os
        PORT = int(os.environ["PORT"])
    except (ValueError, KeyError):
        PORT = 8080

    HTTP_THREAD = threading.Thread(target=run_http_server, args=(PORT,))
    HTTP_THREAD.daemon = True
    HTTP_THREAD.start()

    COMMAND_THREAD = threading.Thread(target=run_commands_executor)
    COMMAND_THREAD.start()
    