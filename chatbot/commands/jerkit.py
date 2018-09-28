import bot
import urllib
import json

# uses JERKCITY
# which is now bonequest
# bonequest.com
def jerkit(body={}, roomId="", sender="", event={}):
    url = "https://www.bonequest.com/api/v2/quote/random/1"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    dialog = data["episodes"][0]["dialog"]
    n = 0;

    output = ""
    for q in dialog:
        output += q[0]
        if len(q) > 0:
            output += ": " + q[1]
        output += "\n"
    #output = data["episodes"][0]["dialog"][0] + ": " + data["episodes"][0]["dialog"][1]
    #output = data["episodes"][0]["dialog"][1]
    return output

bot.COMMANDLIST["jerkit"] = jerkit
bot.HELPLIST["jerkit"] = "retrieves some random nonsense from bonequest.com"
