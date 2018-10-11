from ..command import Command
from ..eventpackage import EventPackage
import bot

class HugCommand(Command):
    def __init__(self):
        self.name = "hug"
        self.help = "1. A person (optional). Because sometimes we all just need a hug."
        self.author = "Skuld"
        self.last_updated = "Oct. 3rd, 2018"

    def run(self, event_pack: EventPackage):
        output = ""
        sender = event_pack.sender
        if len(event_pack.body) == 1:
            output = "* "+bot.theBot.config.matrix["username"]+" hugs "+sender+"\n"
        elif len(event_pack.body) >= 2:
            output = "* "+bot.theBot.config.matrix["username"]+" hugs "+event_pack.body[1]+"\n"

        cur = bot.theBot.mydb.cursor()
        cur.execute("SELECT * FROM hug ORDER BY RAND() LIMIT 1")
        res = cur.fetchall()
        output += res[0][1]

        return output
