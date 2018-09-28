import bot
# chat command $botHelp <command>
# returns String - usage for a specific command
def botHelp(body={}, roomId="", sender="", event={}):
    if( len(body) >= 2):
        helpCommand = body[1]

        if helpCommand in bot.HELPLIST:
            return bot.HELPLIST[helpCommand]
        else:
            return "The command you are looking or can't be found, please try again."
    else:
        return(bot.config.prefix+"help needs at least one argument - the name of another command, ie \""+bot.config.prefix+"help echo\"" \
                "\nFor a list of available commands try \""+bot.config.prefix+"commands\".")

bot.COMMANDLIST["help"] = botHelp
bot.HELPLIST["help"] = "help - 1 accepted, returns information about the use of a given function ie \""+bot.config.prefix+"help help\"."
