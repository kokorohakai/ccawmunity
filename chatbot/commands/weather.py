import bot
import requests
import urllib
import json
import ast
import datetime

def getTemperature(kalvin=""):
    K = float(kalvin)
    F =  9/5 * (K - 273) + 32
    C = K - 273
    output = str(int(F)) + "°F, " + str(int(C)) + "°C"
    return output

def getTime(eTime=0):
    t = datetime.datetime.fromtimestamp(eTime)
    output = t.strftime("%I:%M%p")
    return output

def formatOutput(weather={}):
    output = "Weather for: "
    output += weather["name"] + "\n"

    output += "Condition: "
    output += weather["weather"][0]["description"] + "\n"

    output += "Temperature: "
    output += getTemperature(weather["main"]["temp"]) + "\n"

    output += "  Min/Max: "
    output += getTemperature(weather["main"]["temp_min"]) + " / "
    output += getTemperature(weather["main"]["temp_max"]) + "\n"


    output += "Humidity: "
    output += str(weather["main"]["humidity"]) + "\n"

    output += "Wind Speed: "
    output += str(weather["wind"]["speed"]) + " at " + str(weather["wind"]["deg"]) + "°\n"

    output += "Sunrise / Sunset: "
    output += getTime(weather["sys"]["sunrise"]) + " / "
    output += getTime(weather["sys"]["sunset"])
    return output
# uses openweathermap.com
def weather(body={}, roomId="", sender="", event={}):
    if len(bot.config.weatherkey) > 0:
        baseurl = "https://api.openweathermap.org/data/2.5/weather?"
        body.pop(0)
        city = str("+".join(body))
        citystr = "q=" + city + ",us"
        key = "&appid="+bot.config.weatherkey
        url = baseurl+citystr+key
        data = requests.get(url).json()
        ecode = int(data["cod"])
        if ecode == 404:
            output = data["message"]
        elif ecode == 401:
            output = data["message"]
        elif ecode == 201 or ecode ==  200:
            output = formatOutput(data)
        else:
            output = "An Unknown error occured"
        output +="\n\npowered by openweathermap.org"
    else:
        output = "I'm sorry, the administrator has not added an apikey in the config for this command to work."
    return output

bot.COMMANDLIST["weather"] = weather
bot.HELPLIST["weather"] = "1. a pattern defining your location. Gets the weather information for your supplied location."
