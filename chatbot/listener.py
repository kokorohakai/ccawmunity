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
            True
            #print("{0} joined".format(event['content']['displayname']))
    elif event['type'] == "m.room.message":
        if event['content']['msgtype'] == "m.text":
            #print("{0}: {1}".format(event['sender'], event['content']['body']))

            # ignore anything the bot might send to itself
            if(event['sender'] == "@"+bot.config.username+":cclub.cs.wmich.edu"):
                return

            # split the string to commands
            output =  event['content']['body'].split(" ")

            if ( output[0] == bot.config.username+":" ):
                bot.room.send_text("Hi! I am a bot. If you want to know my commands type \""+bot.config.prefix+"commands\" for available commands")

            # create responses for messages starting with $
            if (output[0][0] == bot.config.prefix and len(output[0]) > 0 ):
                command = output[0][1:]

                # if the command is in our dictionary of functions, use it (from commands.py)
                if command in bot.COMMANDLIST:
                    try:
                        bot.room.send_text(bot.COMMANDLIST[command](body=output, roomId=event["room_id"], sender=event["sender"], event=event))
                    except Exception as e:
                        print(e)
                        bot.room.send_text("This command failed to execute")
    else:
        print(event['type'])
