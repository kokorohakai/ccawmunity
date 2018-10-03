from ..command import Command
from ..eventpackage import EventPackage
import bot

class ContributeCommand(Command):
    def __init__(self):
        self.name = "contribute"
        self.help = "contribute - No parameters required, links the repository url."
        self.author = "Skuld"
        self.last_updated = "Oct. 3rd, 2018"

    def run(self, event_pack: EventPackage):
        output = "If you'd like to contribute a function: https://github.com/kokorohakai/ccawmunity\n"
        output += "This project is a fork of: https://github.com/ccowmu/ccawmunity"
        return output
