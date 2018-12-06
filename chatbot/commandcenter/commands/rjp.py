from ..command import Command
from ..eventpackage import EventPackage
import random
import time
import bot

class RjpCommand(Command):
    def __init__(self):
        self.name = "RJP"
        self.help = "1. Prints a random Japanese word/phrase with English translation.\n"
        self.author = "skuld"
        self.last_updated = "Oct. 11, 2018"

    def getRandom(self):
        cur = bot.theBot.jpdb.cursor()
        sqlStr = "select `entry_id` from `entry-tag` order by rand() limit 1"
        cur.execute( sqlStr )
        results = cur.fetchall()
        id = results[0][0]

        sqlStr = "select * from `entry` "
        sqlStr = sqlStr + "left join `definition` on `definition`.`entry_id` = `entry`.`id` "
        sqlStr = sqlStr + "left join `read` on `read`.`entry_id` = `entry`.`id` "
        sqlStr = sqlStr + "left join `write` on `write`.`entry_id` = `entry`.`id` "
        sqlStr = sqlStr + "where `entry`.`id`=%s and `definition`.`lang` = 'eng' "
        cur.execute(sqlStr,[id])
        definition = cur.fetchall()
        definition = definition[0]

        sqlStr = "select * from `entry-tag` "
        sqlStr = sqlStr + "left join `tag` on `entry-tag`.`tag_id` = `tag`.`id` "
        sqlStr = sqlStr + "where `entry-tag`.`entry_id`=%s"
        cur.execute(sqlStr,[id])
        tags = cur.fetchall()

        if definition[11] == None:
            output = definition[8]
        else:
            output = definition[11] + " (" + definition[8] + ") "
        for i in tags:
            output = output + i[4] + ", " + i[5]
        output = output + definition[4]

        return output

    def run(self, event_pack: EventPackage):
        random.seed(time.time())
        output = self.help

        if len(event_pack.body) == 1:
            output = self.getRandom()

        return output
