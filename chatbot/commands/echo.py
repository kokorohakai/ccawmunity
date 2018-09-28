import bot
# chat command: $echo
# returns String - with all text after $echo separated by spaces
def echo(body={}, roomId="", sender="", event={}):
    if(len(body) >= 2):
        output = " ".join(body[i] for i in range(1, len(body)))
        return output
    else:
        return "Needs more arguments, for example - \"$echo test\""
bot.COMMANDLIST["echo"] = echo
bot.HELPLIST["echo"] = "echo - N parameters accepted separated by spaces, bot echoes them back to chat.\"$echo arg1 arg2\""
