import discord
import bot
from commandcenter import *

class Discord():
    def __init__(self):
        self.discordClient = {}

    def start(self):
        global theBot
        config = bot.theBot.config

        self.discordClient = discord.Client()

        @self.discordClient.event
        async def on_message(message):
            # ignore anything the bot might send to itself
            if message.author == self.discordClient.user:
                return

            #built in auto response to mention.
            if "<@"+self.discordClient.user.id+">" in message.content:
                print("someone metioned Urd")
                msg = "Hi! I am a bot. If you want to know my commands type \""+config.prefix+"commands\" for available commands"
                await self.discordClient.send_message(message.channel, msg)
                return

            # split the string to commands
            input =  message.content.split(" ")

            # create responses for messages starting with prefix
            if len(input) > 0:
                if len(input[0]) > 0:
                    if input[0][0] == config.prefix:
                        command = input[0][1:]

                        ep = commandcenter.EventPackage()
                        ep.body = input
                        ep.room_id = message.channel
                        ep.sender = message.author
                        ep.event = message
                        ep.command = command

                        output = bot.theBot.cc.run(ep)

                        if len(output) > 0:
                            await self.discordClient.send_message( message.channel, output )


        @self.discordClient.event
        async def on_ready():
            print('Logged in as')
            print("  "+self.discordClient.user.name)
            print("  "+self.discordClient.user.id)

    def connect(self):
        global theBot
        config = bot.theBot.config

        #attempt to connect with discord.
        if len(config.discord["token"]) > 0:
            print("discord bot token supplied, attempting to log in.")
            #for some reason this starts it's own blocking loop.
            self.discordClient.run(config.discord["token"])
        return
