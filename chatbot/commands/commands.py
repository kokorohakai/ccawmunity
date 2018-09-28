import settings
# chat command $commands
# returns String - of all the possible bot functions
def commands(body={}, roomId="", sender="", event={}):
   output = " ".join(settings.COMMANDLIST)
   return output
settings.COMMANDLIST["$commands"] = commands
