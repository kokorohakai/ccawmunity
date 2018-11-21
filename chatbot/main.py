#!/usr/bin/env python3
import os
import logging
import time
import signal

from functools import partial
import bot

def shutdown(self,signum):
    print ("Shutting Down")
    global theBot
    bot.theBot.discord.disconnect()
    bot.running = False
    time.sleep(1)
    exit(0)

def main():
    global theBot
    bot.init()
    bot.theBot.dbConnect()
    bot.theBot.go()


if __name__ == '__main__':
    signal.signal(signal.SIGINT,shutdown)
    signal.signal(signal.SIGTERM,shutdown)
    logging.basicConfig(level=logging.WARNING)
    main()
