from ..command import Command
from ..eventpackage import EventPackage

class RoomidCommand(Command):
    def __init__(self):
        self.name = "Room ID"
        self.help = "Prints out a configurable room id for the current channel / Room."
        self.author = "skuld"
        self.last_updated = "Oct 7, 2018"

    def run(self, event_pack: EventPackage):
        return event_pack.room_id
