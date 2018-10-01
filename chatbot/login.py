import bot
import getpass
import sys
from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema

def login():
    config = bot.config

    if config.matrix["password"] == "":
        config.matrix["password"] = getpass.getpass(prompt='Password: ')


    #attempt to log in.
    print("Attempting to log in...")

    try:
        bot.matrixClient.login_with_password(config.matrix["username"], config.matrix["password"])
    except MatrixRequestError as e:
        print(e)
        if e.code == 403:
            print("Bad username or password.")
            sys.exit(4)
        else:
            print("Check your sever details are correct.")
            sys.exit(2)
    except MissingSchema as e:
        print("Bad URL format.")
        print(e)
        sys.exit(3)

    #join the room supplied by the config.
    print("Login Successful, joining room....")

    for room in config.matrix["rooms"]:
        try:
            bot.rooms[room] = bot.matrixClient.join_room(room)
            print("Joined room "+room)
        except MatrixRequestError as e:
            print(e)
            if e.code == 400:
                print("Room ID/Alias in the wrong format")
                sys.exit(11)
            else:
                print("Couldn't find room:"+room)
                sys.exit(12)
