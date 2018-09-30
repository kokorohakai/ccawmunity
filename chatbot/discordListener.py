import discord
import bot
import sys
from commands import *

@bot.discordClient.event
async def on_message(message):
    # ignore anything the bot might send to itself
    if message.author == bot.discordClient.user:
        return

    #built in auto response to mention.
    if "<@"+bot.discordClient.user.id+">" in message.content:
        print("someone metioned Urd")
        msg = "Hi! I am a bot. If you want to know my commands type \""+bot.config.prefix+"commands\" for available commands"
        await bot.discordClient.send_message(message.channel, msg)
        return

    # split the string to commands
    output =  message.content.split(" ")

    # create responses for messages starting with prefix
    if (output[0][0] == bot.config.prefix and len(output[0]) > 0 ):
        command = output[0][1:]

        # if the command is in our dictionary of functions, use it (from commands.py)
        if command in bot.COMMANDLIST:
            try:
                await bot.discordClient.send_message(message.channel, bot.COMMANDLIST[command]( body=output, roomId=message.channel, sender=message.author, event=message ))
            except Exception as e:
                print(e)
                await bot.discordClient.send_message(message.channel,"This command failed to execute")


@bot.discordClient.event
async def on_ready():
    print('Logged in as')
    print("  "+bot.discordClient.user.name)
    print("  "+bot.discordClient.user.id)
