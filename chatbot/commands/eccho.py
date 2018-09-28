import settings
# chat command $eccho
# returns String - a e s t h e t i c echo
def eccho(body={}, roomId="", sender="", event={}):
    return "e c h o"

settings.COMMANDLIST["$eccho"] = eccho
