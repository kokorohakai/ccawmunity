#!/usr/bin/env python3
import sys
import os
import logging
import time


from functools import partial
import bot
from commandcenter import *

def main():
    bot.init()

    if len(sys.argv) > 1:
        bot.theBot.dbConnect()

        commandName = sys.argv[1]
        input = sys.argv
        input.pop(0)

        #cc = commandcenter.CommandCenter()
        bot.theBot.cc.buildList()

        ep = commandcenter.EventPackage()
        ep.body = input
        ep.room_id = "0"
        ep.sender = "console"
        ep.event = {}
        ep.command = commandName

        output = bot.theBot.cc.run(ep)

        if len(output) > 0:
            print(output)
        else:
            print("Command not Found")
    else:
        print("testcommand.py <command> <command arguments>")

if __name__ == '__main__':
    main()
