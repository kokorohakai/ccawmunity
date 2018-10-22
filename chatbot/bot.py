import sys
import time
from config import *
import discord
from matrix_client.client import MatrixClient
from commandcenter import *
import listeners
import mysql.connector
import re

class Bot():
    def __init__(self):
        self.config = Config()
        #app vars
        self.cc = commandcenter.CommandCenter()
        #stuff needed for this and that.
        self.quietmode = False
        self.running = True
        #listeners
        self.matrix = listeners.Matrix()
        self.discord = listeners.Discord()

        self.mydb = {}

        if "-q" in sys.argv:
            f = open(os.devnull, 'w')
            sys.stdout = f
        if "-h" in sys.argv or "--help" in sys.argv:
            print("Usage: chat <options>")
            print("-q : No standard output")
            print("-h : Print Help")
            exit(0)
        return

    def stripPunc(self,inStr):
        outStr = re.sub(r'[\?\.\(\)\!\*\+\=\'\"\^\&\$\#\@\%]',"",inStr)
        return outStr

    def dbConnect(self):
        if len(self.config.mysql["host"]) > 0:
            print("Connecting to Database")
            try:
                self.mydb = mysql.connector.connect(
                    host = self.config.mysql["host"],
                    user = self.config.mysql["user"],
                    passwd = self.config.mysql["passwd"],
                    database = self.config.mysql["database"]
                )
            except:
                print("Could not connect to database.")

    def checkDBConnect(self):
        if not self.mydb.is_connected():
            self.mydb.reconnect()

    def go(self):
        self.cc.buildList()
        #start matrix stuff.
        self.matrix.login()
        self.matrix.listen()
        #start discord stuff.
        self.discord.start()
        self.discord.connect()
        #loop forever until a signal is caught. Sleeping between each iteration so it doesn't consume CPU
        while self.running:
            time.sleep(1)#sleeps 1 second

def init():
    global theBot
    theBot = Bot()
