from ..command import Command
from ..eventpackage import EventPackage
import random
import time

class PurgeCommand(Command):
    def __init__(self):
        self.name = "purge"
        self.help = "Purges messages written by this bot."
        self.author = "skuld"
        self.last_updated = "Oct. 5, 2018"

    def run(self, event_pack: EventPackage):
        output = "unimplemented"
        return output
