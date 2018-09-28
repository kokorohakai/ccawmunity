import botvars 
# chat command $commands
# returns String - of all the possible bot functions
def commands(body={}, roomId="", sender="", event={}):
   output = " ".join(botvars.COMMANDLIST)
   return output
botvars.COMMANDLIST["$commands"] = commands
botvars.HELPLIST["$commands"] = "$commands - No parameters required, lists all available commands."
