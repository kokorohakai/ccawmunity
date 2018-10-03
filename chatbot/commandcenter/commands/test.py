from ..command import Command
from ..eventpackage import EventPackage

class TestCommand(Command):
    def __init__(self):
        self.name = "test"
        self.help = "test | No parameters requirerd."
        self.author = "strongth / skuld"
        self.last_updated = "Sept. 28, 2018"

    def run(self, event_pack: EventPackage):
        return "I'm alive."
