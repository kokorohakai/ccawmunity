#the following looks wrong, but we want the static behaviour
class Config():
    username = "" #The username of the bot.
    password = "" #The password of the bot, if blank, application will prompt for one.
    clienturl = "" #the url of the server you'd like to join.\
    prefix = "$" #the prefix of your commands, this should not be blank. e.g. $help will be the command help.
    room = "" #which room for the bot to join.
