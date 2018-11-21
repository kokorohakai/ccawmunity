from ..command import Command
from ..eventpackage import EventPackage
import bot

class SetCommand(Command):
    def __init__(self):
        self.name = "set"
        self.help = "2. Set A = B. If A is said, B is said in response."
        self.author = "Skuld"
        self.last_updated = "Oct. 5, 2018"

    def run(self, event_pack: EventPackage):
        input = event_pack.body
        input.pop(0)
        input = " ".join(input)
        input = input.split("=")

        output = ""
        if len(input) == 2:
            statement = input[0].lower().strip()
            statement = bot.theBot.stripPunc(statement)

            if len(statement) > 2 and len(input[1]) > 2:
                cur = bot.theBot.mydb.cursor()

                response = input[1].strip()
                room = event_pack.room_id

                sqlStr = "SELECT * FROM response WHERE statement = %s AND room = %s LIMIT 1"
                values = [ statement, room ]
                cur.execute( sqlStr, values )
                myresult = cur.fetchall()

                if len(myresult) > 0:
                    sqlStr = "UPDATE response SET response = %s WHERE statement = %s AND room = %s"
                    values = [ response, statement, room ]
                    cur.execute(sqlStr, values )
                    bot.theBot.mydb.commit()

                else:
                    sqlStr = "INSERT INTO response (room, statement, response) VALUES ( %s, %s, %s )"
                    values = [ room, statement, response ]
                    cur.execute( sqlStr, values )
                    bot.theBot.mydb.commit()

                output = "Okay " + event_pack.sender
            else:
                output = "statement or response not long enough, both have a 3 character minimum."
        else:
            output = "Please supply both a statement and response, with statement = response"
        return output

    def check(str, event_pack: EventPackage):
        input = event_pack.body
        statement = " ".join(input).strip().lower();
        statement = bot.theBot.stripPunc(statement)

        room = event_pack.room_id

        cur = bot.theBot.mydb.cursor()
        sqlStr = "SELECT * FROM response WHERE statement = %s AND room = %s LIMIT 1"
        values = [ statement, room ]
        cur.execute( sqlStr, values )
        myresult = cur.fetchall()

        output = ""
        if len(myresult) > 0:
            output = myresult[0][2];

        return output

'''
    table Structure for your database:

    CREATE TABLE response (
        id BIGINT(64) unsigned NOT NULL AUTO_INCREMENT,
        room TEXT,
        statement TEXT,
        response TEXT,
        PRIMARY KEY (id)
    );
'''
