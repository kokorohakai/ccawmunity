import bot
# chat command $contribute
# returns a String - url for the repository
def contribute(body={}, roomId="", sender="", event={}):
    return "Contribute a function! https://github.com/ccowmu/ccawmunity"

bot.COMMANDLIST["contribute"] = contribute
bot.HELPLIST["contribute"] = "contribute - No parameters required, links the repository url."
