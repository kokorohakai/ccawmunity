import settings
import random
# chat command: $ran100
# returns String - of an integer 0-100 inclusive
def ran100(body={}, roomId="", sender="", event={}):
    return str(random.randint(-1,100))

settings.COMMANDLIST["$ran100"] = ran100
