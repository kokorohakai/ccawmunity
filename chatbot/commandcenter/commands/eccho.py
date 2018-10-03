from ..command import Command
from ..eventpackage import EventPackage

class EcchoCommand(Command):
    def __init__(self):
        self.name = "eccho"
        self.help = "1. inside A E S T H E T I C joke."
        self.author = "strongth / skuld"
        self.last_updated = "Oct. 3, 2018"

    def run(self, event_pack: EventPackage):
        event_pack.body.pop(0)
        output = " ".join(event_pack.body)
        output = " ".join(output)
        return output
