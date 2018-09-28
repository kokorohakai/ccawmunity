import botvars
# chat command $eccho
# returns String - a e s t h e t i c echo
def eccho(body={}, roomId="", sender="", event={}):
    return "e c h o"

botvars.COMMANDLIST["$eccho"] = eccho
botvars.HELPLIST["$eccho"] = "$eccho - No parameters required, inside A E S T H E T I C joke.",
    
