import botvars
import random
# chat command: $ran100
# returns String - of an integer 0-100 inclusive
def ran100(body={}, roomId="", sender="", event={}):
    return str(random.randint(-1,100))

botvars.COMMANDLIST["$ran100"] = ran100
botvars.HELPLIST["$ran100"] = "$random - No parameters required, returns number 0-100 inclusive."
