from ..command import Command
from ..eventpackage import EventPackage

class TogeCommand(Command):
    def __init__(self):
        self.name = "toge"
        self.help = "1. Adds Emphasis to your speech."
        self.author = "skuld"
        self.last_updated = "Oct. 3, 2018"

    def run(self, event_pack: EventPackage):
        event_pack.body.pop(0)
        output = "`" + " ".join(event_pack.body).upper() + "!`"
        return output
