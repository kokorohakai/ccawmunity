import settings
# chat command: $echo
# returns String - with all text after $echo separated by spaces
def echo(body={}, roomId="", sender="", event={}):
    if(len(body) >= 2):
        output = " ".join(body[i] for i in range(1, len(body)))
        return output
    else:
        return "Needs more arguments, for example - \"$echo test\""
settings.COMMANDLIST["$echo"] = echo
