import bot
import sys
from commands import *
from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema

# called when a message is recieved.
def listener(room, event):
    if event['type'] == "m.room.member":
        if event['membership'] == "join":
            print("{0} joined".format(event['content']['displayname']))
    elif event['type'] == "m.room.message":
        if event['content']['msgtype'] == "m.text":
            print("{0}: {1}".format(event['sender'], event['content']['body']))

            # ignore anything the bot might send to itself
            if(event['sender'] == "@"+bot.config.username+":cclub.cs.wmich.edu"):
                return

            # create responses for messages starting with $
            if(event['content']['body'][0] == '$'):

                output = event['content']['body'].split(" ")
                command = output[0]

                # if the command is in our dictionary of functions, use it (from commands.py)
                if command in bot.COMMANDLIST:
                    bot.room.send_text(bot.COMMANDLIST[command](body=output, roomId=event["room_id"], sender=event["sender"], event=event))
                else:
                    bot.room.send_text("Command not recognized, please try \"$commands\" for available commands")
    else:
        print(event['type'])
