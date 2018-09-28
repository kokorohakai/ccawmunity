import settings
# chat command $botHelp <command>
# returns String - usage for a specific command
def botHelp(body={}, roomId="", sender="", event={}):
    if(len(body) >= 2):
        if(body[1] in HELPLIST):
            return HELPLIST[body[1]]
        else:
            return "The command you are looking or can't be found, please try again."
    else:
        return("$help needs at least one argument - the name of another command, ie \"$help $echo\"" \
                "\nFor a list of available commands try \"$commands\".")
settings.COMMANDLIST["$help"] = botHelp
