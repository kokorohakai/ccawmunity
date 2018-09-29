#!/usr/bin/env python3
import sys
import os
import logging
import time
import signal

from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema

from functools import partial
import bot
from listener import *
from login import *

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command in bot.COMMANDLIST:
            output = sys.argv
            output.pop(0)
            print( bot.COMMANDLIST[command]( body=output, roomId="0", sender="console", event="command") )
        else:
            print("command does not exist")
    else:
        print("testcommand.py <command> <command arguments>")

if __name__ == '__main__':
    main()
