from ..command import Command
from ..eventpackage import EventPackage
import bot

class ForgetCommand(Command):
    def __init__(self):
        self.name = "forget"
        self.help = "1. statement. Forget a response to statement set by .set"
        self.author = "Skuld"
        self.last_updated = "Oct. 5, 2018"

    def run(self, event_pack: EventPackage):
        input = event_pack.body
        input.pop(0)
        statement = " ".join(input).strip().lower();

        room = event_pack.room_id

        cur = bot.theBot.mydb.cursor()
        sqlStr = "DELETE FROM response WHERE statement = %s AND room = %s"
        values = [ statement, room ]
        cur.execute( sqlStr, values )
        bot.theBot.mydb.commit()

        if cur.rowcount > 0:
            output = "I forgot " + statement
        else:
            output = "What's " + statement + "?"

        return output

'''
    table Structure for your database:

    CREATE TABLE response (
        id BIGINT(64) unsigned NOT NULL AUTO_INCREMENT,
        room TEXT,
        statement TEXT,
        response TEXT,
        UNIQUE KEY SHA2(statement),
        PRIMARY KEY (id)
    );
'''
