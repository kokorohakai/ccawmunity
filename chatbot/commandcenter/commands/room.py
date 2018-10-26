from ..command import Command
from ..eventpackage import EventPackage
import random
import time
import bot

class RoomCommand(Command):
    def __init__(self):
        self.name = "Room"
        self.help = "1. Prints Users in the room. \n"
        self.help = self.help + "2. in. Checks in to the room. \n"
        self.help = self.help + "2. out. Checks out of the room. \n"
        self.help = self.help + "2. status. Tells you whether you are in or out. \n"
        self.author = "skuld"
        self.last_updated = "Oct. 26, 2018"
        self.cur = bot.theBot.mydb.cursor()

    def checkStatus(self, event_pack):
        output = False
        sqlStr = "SELECT * FROM room WHERE user = %s ORDER BY id DESC LIMIT 1"
        values = [ event_pack.sender ]
        self.cur.execute(sqlStr, values)
        result = self.cur.fetchall()
        if (len(result) > 0):
            if result[0][3] == None:
                output = True
            else:
                output = False
        return output

    def checkout( self, event_pack ):
        output = "You are not checked in."
        sqlStr = "SELECT * FROM room WHERE user = %s ORDER BY id DESC LIMIT 1"
        values = [ event_pack.sender ]
        self.cur.execute(sqlStr, values)
        result = self.cur.fetchall()

        if len(result) > 0:
            id = result[0][0]
            if result[0][3] == None:
                sqlStr = "UPDATE room SET timeout = NOW() WHERE id = %s"
                values = [ id ]
                self.cur.execute( sqlStr, values )
                bot.theBot.mydb.commit()
                output = "Checked out."

        return output

    def checkin(self, event_pack):
        output = "Couldn't check in."
        if not self.checkStatus( event_pack ):
            sqlStr = "INSERT INTO room ( user, timein ) VALUES (%s,NOW())"
            values = [ event_pack.sender ]
            self.cur.execute( sqlStr, values )
            bot.theBot.mydb.commit()
            output = "Checked in!"
        else:
            output = "Couldn't check in - reason: you are already checked in."

        return output

    def listRoom(self, event_pack):
        output = "The following users are in the room:\n"
        sqlStr = "SELECT DISTINCT user FROM room WHERE timeout IS NULL"
        self.cur.execute(sqlStr)
        result = self.cur.fetchall()

        n = 0
        while n < len(result):
            output = output + result[n][0] + " "
            n = n + 1

        return output

    def status(self, event_pack):
        output = "Out of the room."
        if self.checkStatus( event_pack ):
            output = "In the room."

        return output

    def run(self, event_pack: EventPackage):
        output = self.help
        self.cur = bot.theBot.mydb.cursor()

        if len(event_pack.body) == 1:
            output = self.listRoom(event_pack)
        elif len(event_pack.body) == 2:
            if event_pack.body[1] == "in":
                output = self.checkin(event_pack)
            elif event_pack.body[1] == "out":
                output = self.checkout(event_pack)
            elif event_pack.body[1] == "status":
                output = self.status(event_pack)

        return output
