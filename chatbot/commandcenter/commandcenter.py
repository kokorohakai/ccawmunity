import sys
import inspect
import commandcenter.commands
from commandcenter.eventpackage import *
import bot

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

            if offend in output:
                return True
            n = n + 1
        return False

    def run(self, eventpackage: EventPackage):
        config = bot.theBot.config
        output = ""

        tries = 0
        offensive = True

        if eventpackage.command.startswith(config.prefix):
            while offensive and tries < 5:
                eventpackage.command = eventpackage.command.replace(config.prefix,"")
                if eventpackage.command in self.commandList:
                    if eventpackage.command in config.commandFilter:
                        if eventpackage.room_id in config.commandFilter[eventpackage.command]:
                            output = self.actuallyRun(eventpackage)
                    else:
                        output = self.actuallyRun(eventpackage)
                offensive = self.checkOffensive(output)
                tries=tries+1
        else:
            while offensive and tries < 5:
                output = self.commandList["set"].check(eventpackage);
                offensive = self.checkOffensive(output)
                tries=tries+1

        if offensive:
            output = "I am forbidden to say the result of that command."

        return output
