from ..command import Command
from ..eventpackage import EventPackage
import bot
import random

class HugCommand(Command):
    def __init__(self):
        self.name = "hug"
        self.help = "1. A person (optional). Because sometimes we all just need a hug."
        self.author = "Skuld"
        self.last_updated = "Oct. 3rd, 2018"

    def run(self, event_pack: EventPackage):
        output = ""
        sender = event_pack.sender
        print(sender)
        if len(event_pack.body) == 1:
            output = "* "+bot.theBot.config.matrix["username"]+" hugs "+sender+"\n"
        elif len(event_pack.body) >= 2:
            output = "* "+bot.theBot.config.matrix["username"]+" hugs "+event_pack.body[1]+"\n"

        n = random.randint( 0, len(bot.theBot.config.hug["replies"])-1)
        output += bot.theBot.config.hug["replies"][n]

        return output
