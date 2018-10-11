from ..command import Command
from ..eventpackage import EventPackage
import bot

class HelpCommand(Command):
    def __init__(self):
        self.name = "help"
        self.help = "1. the command. Prints help for specified command."
        self.author = "Skuld"
        self.last_updated = "Oct. 3, 2018"

    def run(self, event_pack: EventPackage):
        name = ""
        if len(event_pack.body) > 1:
            name = event_pack.body[1]
        if name in bot.theBot.cc.commandList:
            output = bot.theBot.cc.commandList[name].help
        else:
            output = "Command does not exist"
        return output
