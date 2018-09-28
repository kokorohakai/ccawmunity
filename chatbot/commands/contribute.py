import settings
# chat command $contribute
# returns a String - url for the repository
def contribute(body={}, roomId="", sender="", event={}):
    return "Contribute a function! https://github.com/ccowmu/ccawmunity"

settings.COMMANDLIST["$contribute"] = contribute
