import bot
import random
import time
# chat command: $ran100
# returns String - of an integer 0-100 inclusive
def rand(body={}, roomId="", sender="", event={}):
    value = "Please use 0-3 arguments."
    random.seed(time.time())
    if ( len(body) == 1 ):
        value = str( random.randint( 0, 100 ) )
    if ( len(body) == 2 ):
        value = str( random.randint( 0, int(body[1]) ) )
    if ( len(body) == 3 ):
        value = str( random.randint( int(body[1]), int(body[2]) ) )
    if ( len(body) == 4 ):
        value = ""
        for t in range( 0, int(body[3]) ):
            value += " " +  str( random.randint( int(body[1]), int(body[2]) ) )
    return value

bot.COMMANDLIST["random"] = rand
bot.HELPLIST["random"] = "random: random number from 0 to 100\n"
bot.HELPLIST["random"] += "random n: random number from 0 to n\n"
bot.HELPLIST["random"] += "random m n: random number mfrom m to n\n"
bot.HELPLIST["random"] += "random m n t: t random numbers from m to n\n"
