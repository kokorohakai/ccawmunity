import bot
# chat command: $test
# returns String - yelling at dolphin
def test(body={}, roomId="", sender="", event={}):
    return "Why would you have a test command, DOLPHIN?"

bot.COMMANDLIST["$test"] = test
bot.HELPLIST["$test"] = "$test - No parameters requirerd, yells at dolphin."
