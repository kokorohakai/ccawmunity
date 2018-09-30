from config import *
import discord
from matrix_client.client import MatrixClient

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
global matrixClient
#initialze the client for the bot.
matrixClient = MatrixClient(config.clienturl)

#discord client variables
global discordClient
discordClient = discord.Client()

#other application variables
quietmode = False
global running
running = True
