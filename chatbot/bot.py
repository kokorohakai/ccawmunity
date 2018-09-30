from config import *
import discord

#command parsing variables
global HELPLIST
HELPLIST = {}
global COMMANDLIST
COMMANDLIST = {}
global quietmode
global config
#user config.
config = Config
#matrix client variables.
global room
global client
#discord client variables
global discordClient
discordClient = discord.Client()

#other application variables
quietmode = False
global running
running = True
