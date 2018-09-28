import botvars
# chat command: $test
# returns String - yelling at dolphin
def test(body={}, roomId="", sender="", event={}):
    return "Why would you have a test command, DOLPHIN?"

botvars.COMMANDLIST["$test"] = test
botvars.HELPLIST["$test"] = "$test - No parameters requirerd, yells at dolphin."
