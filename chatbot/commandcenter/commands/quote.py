from ..command import Command
from ..eventpackage import EventPackage
import random
import time
import bot

class QuoteCommand(Command):
    def __init__(self):
        self.name = "Quote"
        self.help = "1. Prints a random quote\n" +
                    "2. user. Prints a random quote by the supplied user.\n" +
                    "3. remove, id. Removes a quote by id." +
                    "4. add, user, quote. Adds a quote for user.\n"
        self.author = "skuld"
        self.last_updated = "Oct. 11, 2018"

    def add(self,user,quote):
        output = "Failed to add"

        cur = bot.theBot.mydb.cursor()

        sqlStr = "SELECT * FROM quotes WHERE user = %s and quote = %s LIMIT 1"
        values = [ user, quote ]
        cur.execute( sqlStr, values )
        myresult = cur.fetchall()

        if len(myresult) > 0:
            output = "This user already has this quote."
        else:
            sqlStr = "INSERT INTO quotes (user, quote) VALUES ( %s, %s )"
            values = [ user, quote ]
            cur.execute( sqlStr, values )
            bot.theBot.mydb.commit()

            output = "Added quote for "+user
        return output

    def remove(self, id):
        output = "removed"

        cur = bot.theBot.mydb.cursor()
        sqlStr = "DELETE FROM quotes WHERE id = %s"
        values = [ id ]
        cur.execute( sqlStr, values )
        bot.theBot.mydb.commit()

        if cur.rowcount > 0:
            output = "The quote was removed."
        else:
            output = "I could not find this quote to remove it."

        return output

    def getRandomByUser(self, user):
        output = "Could not find a quote by that user."

        cur = bot.theBot.mydb.cursor()
        sqlStr = "select count(*) FROM quotes"
        cur.execute( sqlStr )
        myresult = cur.fetchall()
        n = random.randint( 0, myresult[0][0]-1 )

        sqlStr = 'SELECT id,quote FROM quotes WHERE user = %s LIMIT ' + str(n) + ',1'
        values = [ user ]
        cur.execute( sqlStr, values )
        myresult = cur.fetchall()
        if len(myresult) > 0:
            if len(myresult[0]) > 0:
                output = "(" + str(myresult[0][0]) + "): " + myresult[0][1]

        return output

    def getRandom(self):
        output = "Could not find a quote."

        cur = bot.theBot.mydb.cursor()
        sqlStr = "select count(*) FROM quotes"
        cur.execute( sqlStr )
        myresult = cur.fetchall()
        n = random.randint( 0, myresult[0][0]-1 )

        sqlStr = "SELECT id,user,quote FROM quotes LIMIT "+str(n)+",1"
        cur.execute( sqlStr )
        myresult = cur.fetchall()
        if len(myresult) > 0:
            if len(myresult[0]) > 0:
                output = "(" + str(myresult[0][0]) + ") - " + myresult[0][1] + ': "' + myresult[0][2] + '"'

        return output

    def run(self, event_pack: EventPackage):
        random.seed(time.time())
        output = self.help

        if len(event_pack.body) == 1:
            output = self.getRandom()
        elif len(event_pack.body) == 2:
            user = event_pack.body[1].lower()
            output = self.getRandomByUser(user)
        elif len(event_pack.body) == 3:
            if event_pack.body[1] == "remove":
                id = event_pack.body[2]
                output = self.remove(id)
        elif len(event_pack.body) > 3:
            if event_pack.body[1] == "add":
                user = event_pack.body[2].lower()
                quote = event_pack.body
                quote.pop(0)
                quote.pop(0)
                quote.pop(0)
                quote = " ".join(quote).strip()
                output = self.add(user,quote)
        return output
