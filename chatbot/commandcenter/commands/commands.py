from ..command import Command
from ..eventpackage import EventPackage
import bot

class CommandsCommand(Command):
    def __init__(self):
        self.name = "commands"
        self.help = "commands - No parameters required, lists all available commands."
        self.author = "Skuld"
        self.last_updated = "Oct. 3rd, 2018"

    def run(self, event_pack: EventPackage):
        output = "I response to the following commands:\n"
        for name in bot.theBot.cc.commandList:
            output += bot.theBot.config.prefix + name + " "
        return output
