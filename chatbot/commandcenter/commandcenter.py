import sys
import inspect
import commandcenter.commands
from commandcenter.eventpackage import *
import bot
import copy

class CommandCenter():
    def __init__(self):
        self.commandList = {}
        return
    def buildList(self):
        #use this to finish writing the code of the bot.
        cprefix = "commandcenter.commands."
        for module in sys.modules:
            if module.startswith(cprefix):
                commandName = module.replace(cprefix,"")
                classname = commandName.capitalize()+"Command"
                found = False
                for name,obj in inspect.getmembers(sys.modules[module]):
                    if name == classname:
                        self.commandList[commandName] = obj()
                        print( "Loaded Command:"+commandName )
                        found = True
                if not found:
                    print( "Malformed Command: "+commandName+" could not find class named "+classname)

    def actuallyRun(self, eventpackage: EventPackage):
        try:
            output = self.commandList[eventpackage.command].run(eventpackage)
        except Exception as e:
            print(e)
            output = "This command failed to execute"
        return output

    def getOffensive(self):
        cur = bot.theBot.mydb.cursor()

        sqlStr = "SELECT * FROM offensive"
        cur.execute(sqlStr)
        res = cur.fetchall()
        return res

    def checkOffensive(self, output):
        check = " " + bot.theBot.stripPunc(output) + " " #we need to add the spaces to check if the phrase exists reliably. They will not be added in the output.
        checklist = self.getOffensive()
        n = 0
        l = len(checklist)
        while n < l:
            offend = " " + checklist[n][1] + " "
            if offend in check:
                return True
            n = n + 1
        return False

    def run(self, eventpackage: EventPackage):
        config = bot.theBot.config
        output = ""

        tries = 0
        offensive = True

        while offensive and tries < 5:
            newep = copy.copy(eventpackage)
            newep.event = copy.copy(eventpackage.event)
            newep.body = copy.copy(eventpackage.body)

            if newep.command.startswith(config.prefix):
                newep.command = newep.command.replace(config.prefix,"")
                if newep.command in self.commandList:
                    if newep.command in config.commandFilter:
                        if newep.room_id in config.commandFilter[newep.command]:
                            output = self.actuallyRun(newep)
                    else:
                        output = self.actuallyRun(newep)
                else:
                    offensive = False
                    output = ""
            else:
                output = self.commandList["set"].check(newep);

            offensive = self.checkOffensive(output)
            tries = tries + 1

        if offensive:
            output = "I am forbidden to say the result of that command."

        return output
