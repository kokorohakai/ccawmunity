from ..command import Command
from ..eventpackage import EventPackage

class WhoamiCommand(Command):
    def __init__(self):
        self.name = "Who Am I?"
        self.help = "Prints out a configurable name for you."
        self.author = "skuld"
        self.last_updated = "Oct 11, 2018"

    def run(self, event_pack: EventPackage):
        return event_pack.sender
