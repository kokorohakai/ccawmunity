#Fill in the following variables with your credentials and save to config.py
class Config():
    #matrix / riot
    username = "" #The username of the bot.
    password = "" #The password of the bot, if blank, application will prompt for one.
    clienturl = "" #the url of the server you'd like to join.\
    prefix = "$" #the prefix of your commands, this should not be blank. e.g. $help will be the command help.
    room = "" #which room for the bot to join.
    #discord
    token = ""
    #Open weather
    weatherkey = ""
    #mysql connection. If it exists, bot will try to connect with supplied credentials.
    mysql = {
        "host": "",
        "user": "",
        "passwd": "",
        "database":""
        "jp-database":""#only required for the rjp command.
    }
    commandFilter = { #If specified, filters a command to certain rooms / channels.
        #find the room id with .roomid
        #"command":["A","B"] #for example, command can now only be used in #A or #B

    }
    admins=[ #the admin list, make sure to add your users from both matrix and discord.
            ""
    ]
