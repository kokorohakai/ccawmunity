from ..command import Command
from ..eventpackage import EventPackage
import bot

class OffensiveCommand(Command):
    def __init__(self):
        self.name = "offensive"
        self.help = "1. add or remove.\n"
        self.help += bot.theBot.config.prefix+"offensive add word - adds word to the offensive list.\n"
        self.help += bot.theBot.config.prefix+"offensive remove word - adds word to the offensive list.\n"
        self.author = "skuld"
        self.last_updated = "Oct. 5, 2018"

    def add(self,phrase):
        output = "Failed to add"

        cur = bot.theBot.mydb.cursor()

        sqlStr = "SELECT * FROM offensive WHERE phrase = %s LIMIT 1"
        values = [ phrase ]
        cur.execute( sqlStr, values )
        myresult = cur.fetchall()

        if len(myresult) > 0:
            output = "This phrase is already in my list of offensive phrases.\n"
            output += "Maybe try to reword it?"

        else:
            sqlStr = "INSERT INTO offensive (phrase) VALUES ( %s )"
            values = [ phrase ]
            cur.execute( sqlStr, values )
            bot.theBot.mydb.commit()

            output = "Phrase was added to offensive list.\n"
            output += "I'll make sure I don't say it again. Sorry."

        return output

    def remove(self,phrase):
        output = "removed"

        cur = bot.theBot.mydb.cursor()
        sqlStr = "DELETE FROM offensive WHERE phrase = %s"
        values = [ phrase ]
        cur.execute( sqlStr, values )
        bot.theBot.mydb.commit()

        if cur.rowcount > 0:
            output = "The phrase was removed from the offensive list."
        else:
            output = "This phrase did not exist."

        return output

    def run(self, event_pack: EventPackage):
        #I need some way to check if this command is from an admin.
        output = self.help
        if len( event_pack.body ) > 2:
            command = event_pack.body[1].lower()
            phraseA = event_pack.body
            phraseA.pop(0)
            phraseA.pop(0)
            phrase = " ".join(phraseA)

            if command == "add":
                output = self.add(phrase)
            if command == "remove":
                output = self.remove(phrase)

        return output
