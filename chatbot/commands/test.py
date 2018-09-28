import settings
# chat command: $test
# returns String - yelling at dolphin
def test(body={}, roomId="", sender="", event={}):
    return "Why would you have a test command, DOLPHIN?"

settings.COMMANDLIST["$test"] = test
