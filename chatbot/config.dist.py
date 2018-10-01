#the following looks wrong, but we want the static behaviour
class Config():
    prefix = "$"
    matrix = {
        "username": "", #The username of the bot.
        "password": "", #The password of the bot, if blank, application will prompt for one.
        "clienturl": "", #the url of the server you'd like to join.\
        "rooms": [ #which rooms for the bot to join.
            ""
        ]
    }
    discord = {
        "token": "" #Your discord bot token.
    }
    weather = {
        "key": "",#your openweathermap api key.
        "country": "",#what country are we looking at weather in.
        "city":"" #if supplied, this is the default city the weather searches
    }
    hug = {
        "replies": [ #an array of possible replies. Fill in your own!
            "There there little buddy, it'll be alright."
        ]
    }
