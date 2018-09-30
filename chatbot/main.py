#!/usr/bin/env python3

# A simple chat client for matrix.
# This sample will allow you to connect to a room, and send/recieve messages.
# Args: host:port username password room
# Error Codes:
# 1 - Unknown problem has occured
# 2 - Could not find the server.
# 3 - Bad URL Format.
# 4 - Bad username/password.
# 11 - Wrong room format.
# 12 - Couldn't find room.

import sys
import os
import logging
import time
import signal
import discord

from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema

from functools import partial
import bot
from listener import *
from discordListener import *
from login import *

def shutdown(self,signum):
    print ("Shutting Down")
    bot.running = False
    time.sleep(1)
    exit(0)

def main():
    #parses arguments passed into the application.
    #We may want to make this a function on it's own that handles this in a single pass, instead of scanning it each time for possible values.
    if "-q" in sys.argv:
        f = open(os.devnull, 'w')
        sys.stdout = f
    if "-h" in sys.argv or "--help" in sys.argv:
        print("Usage: chat <options>")
        print("-q : No standard output")
        print("-h : Print Help")
        exit(0)

    #initialze the client for the bot.
    bot.client = MatrixClient(bot.config.clienturl)

    #attempt to login.
    login()

    #attempt to connect with discord.
    if len(bot.config.token) > 0:
        print("discord bot token supplied, attempting to log in.")
        bot.discordClient.run(bot.config.token)


    #if success, start the command listener.
    bot.room.add_listener(listener)
    bot.client.start_listener_thread()

    #loop forever until a signal is caught. Sleeping between each iteration so it doesn't consume CPU
    while bot.running:
        time.sleep(1)#sleeps 1 second

if __name__ == '__main__':
    signal.signal(signal.SIGINT,shutdown)
    signal.signal(signal.SIGTERM,shutdown)
    logging.basicConfig(level=logging.WARNING)
    main()
