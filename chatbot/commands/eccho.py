import bot
# chat command $eccho
# returns String - a e s t h e t i c echo
def eccho(body={}, roomId="", sender="", event={}):
    instr = body[1]
    outstr = " ".join(instr)
    return outstr

bot.COMMANDLIST["eccho"] = eccho
bot.HELPLIST["eccho"] = "eccho - 1. inside A E S T H E T I C joke."
