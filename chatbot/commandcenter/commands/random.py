from ..command import Command
from ..eventpackage import EventPackage
import random
import time

class RandomCommand(Command):
    def __init__(self):
        self.name = "random"
        self.help = "random: random number from 0 to 100\n"
        self.help = self.help + "random n: random number from 0 to n\n"
        self.help = self.help + "random m n: random number mfrom m to n\n"
        self.help = self.help + "random m n t: t random numbers from m to n\n"
        self.author = "skuld"
        self.last_updated = "Oct. 3, 2018"

    def run(self, event_pack: EventPackage):
        value = "Please use 0-3 arguments."
        random.seed(time.time())

        length = len(event_pack.body)

        if ( length == 1 ):
            value = str( random.randint( 0, 100 ) )
        if ( length == 2 ):
            value = str( random.randint( 0, int(event_pack.body[1]) ) )
        if ( length == 3 ):
            value = str( random.randint( int(event_pack.body[1]), int(event_pack.body[2]) ) )
        if ( length == 4 ):
            value = ""
            for t in range( 0, int(event_pack.body[3]) ):
                value += " " +  str( random.randint( int(event_pack.body[1]), int(event_pack.body[2]) ) )
        return value

        event_pack.body.pop(0)
        output = "`" + " ".join(event_pack.body).upper() + "!`"
        return output
