import bot
import random

# chat command: $echo
# returns String - with all text after $echo separated by spaces
def hug(body={}, roomId="", sender="", event={}):
    output = ""
    print(sender)
    if len(body) == 1:
        output = "* "+bot.config.matrix["username"]+" hugs "+sender+"\n"
    elif len(body) >= 2:
        output = "* "+bot.config.matrix["username"]+" hugs "+body[1]+"\n"

    n = random.randint( 0, len(bot.config.hug["replies"])-1)
    output += bot.config.hug["replies"][n]

    return output

bot.COMMANDLIST["hug"] = hug
bot.HELPLIST["hug"] = "hug - 1. A person. Because sometimes we all just need a hug."
