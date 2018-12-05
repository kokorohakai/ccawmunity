import sys
from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema
import bot
from commandcenter import *


class Matrix():
    def __init__(self):
        self.rooms = {}
        self.matrixClient = {}

    def login(self):
        global theBot
        config = bot.theBot.config

        #variables
        self.matrixClient = MatrixClient(config.matrix["clienturl"])

        if config.matrix["password"] == "":
            config.matrix["password"] = getpass.getpass(prompt='Password: ')


        #attempt to log in.
        print("Attempting to log in...")

        try:
            self.matrixClient.login_with_password(config.matrix["username"], config.matrix["password"])
        except MatrixRequestError as e:
            print(e)
            if e.code == 403:
                print("Bad username or password.")
                sys.exit(4)
            else:
                print("Check your sever details are correct.")
                sys.exit(2)
        except MissingSchema as e:
            print("Bad URL format.")
            print(e)
            sys.exit(3)

        #join the room supplied by the config.
        print("Login Successful, joining room....")

        for room in config.matrix["rooms"]:
            try:
                self.rooms[room] = self.matrixClient.join_room(room)
                print("Joined room "+room)
            except MatrixRequestError as e:
                print(e)
                if e.code == 400:
                    print("Room ID/Alias in the wrong format")
                    sys.exit(11)
                else:
                    print("Couldn't find room:"+room)
                    sys.exit(12)
    def eatMe( self, exception ):
        print ("An Error occured, ignoring")
        return

    def listen(self):
        global theBot
        config = bot.theBot.config

        #if success, start the command listener.
        for i in self.rooms:
            self.rooms[i].add_listener(self.listener)
        #self.matrixClient.listen_forever(exception_handler = self.eatMe);
        self.matrixClient.start_listener_thread()

    def listener(self, room, event):
        global theBot
        config = bot.theBot.config

        if event['type'] == "m.room.message":
            if event['content']['msgtype'] == "m.text":
                #print("{0}: {1}".format(event['sender'], event['content']['body']))

                # ignore anything the bot might send to itself
                if(event['sender'] == "@"+config.matrix["username"]+":cclub.cs.wmich.edu"):
                    return

                #built in auto response to mention.
                if ( config.matrix["username"] + ":" in event['content']['body']):
                    room.send_text("Hi! I am a bot. If you want to know my commands type \""+config.prefix+"commands\" for available commands")

                # split the string to commands
                input = event['content']['body'].split(" ")

                # create responses for messages starting with prefix
                if len(input) > 0:
                    if len(input[0]) > 0:
                        ep = commandcenter.EventPackage()
                        ep.body = input
                        ep.room_id = event["room_id"]
                        ep.sender = event["sender"]
                        ep.event = event
                        ep.command = input[0]
                        if ep.command == config.prefix+"purge":
                            self.purge(ep)
                        else:
                            output = bot.theBot.cc.run(ep)

                            # if the command is in our dictionary of functions, use it (from commands.py)
                            if len(output) > 0:
                                room.send_text(output)

        else:
            print(event['type'])

    def purge(self, event ):
        return
