from ..command import Command
from ..eventpackage import EventPackage
import bot
import requests
import urllib
import json
import ast
import datetime

class WeatherCommand(Command):
    def __init__(self):
        self.name = "weather"
        self.help = "1. a pattern defining your location (optional). Gets the weather information for your supplied location."
        self.author = "Skuld"
        self.last_updated = "Oct. 3rd, 2018"

    def getTemperature(self,kalvin=""):
        K = float(kalvin)
        F =  9/5 * (K - 273) + 32
        C = K - 273
        output = str(int(F)) + "°F, " + str(int(C)) + "°C"
        return output

    def getTime(self,eTime=0):
        t = datetime.datetime.fromtimestamp(eTime)
        output = t.strftime("%I:%M%p")
        return output

    def formatOutput(self,weather={}):
        output = "Weather for: "
        output += weather["name"] + "\n"

        output += "Condition: "
        output += weather["weather"][0]["description"] + "\n"

        output += "Temperature: "
        output += self.getTemperature(weather["main"]["temp"]) + "\n"

        output += "  Min/Max: "
        output += self.getTemperature(weather["main"]["temp_min"]) + " / "
        output += self.getTemperature(weather["main"]["temp_max"]) + "\n"


        output += "Humidity: "
        output += str(weather["main"]["humidity"]) + "\n"

        output += "Wind Speed: "
        output += str(weather["wind"]["speed"]) + " at " + str(weather["wind"]["deg"]) + "°\n"

        output += "Sunrise / Sunset: "
        output += self.getTime(weather["sys"]["sunrise"]) + " / "
        output += self.getTime(weather["sys"]["sunset"])
        return output

    def run(self, event_pack: EventPackage):
        if len(bot.theBot.config.weather["key"]) > 0:
            baseurl = "https://api.openweathermap.org/data/2.5/weather?"
            body = event_pack.body
            body.pop(0)
            #set the city
            city = str("+".join(body))
            if (len(city) < 1):
                city = bot.theBot.config.weather["city"]
            citystr = "q=" + city
            if len(bot.theBot.config.weather["country"]) > 0:
                citystr += ",us"
            #set the key
            key = "&appid="+bot.theBot.config.weather["key"]
            #set the url and get our data
            url = baseurl+citystr+key
            data = requests.get(url).json()
            #time to format the output.
            ecode = int(data["cod"])
            if ecode == 404:
                output = data["message"]
            elif ecode == 401:
                output = data["message"]
            elif ecode == 201 or ecode ==  200:
                output = self.formatOutput(data)
            else:
                output = "An Unknown error occured"
            output +="\n\npowered by openweathermap.org"
        else:
            output = "I'm sorry, the administrator has not added an apikey in the config for this command to work."
        return output
