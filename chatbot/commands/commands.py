import bot 
# chat command $commands
# returns String - of all the possible bot functions
def commands(body={}, roomId="", sender="", event={}):
   output = " ".join(bot.COMMANDLIST)
   return output
bot.COMMANDLIST["$commands"] = commands
bot.HELPLIST["$commands"] = "$commands - No parameters required, lists all available commands."
