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

    def run(self, eventpackage: EventPackage):
        config = bot.theBot.config
        output = ""

        if eventpackage.command.startswith(config.prefix):
            eventpackage.command = eventpackage.command.replace(config.prefix,"")
            if eventpackage.command in self.commandList:
                if eventpackage.command in config.commandFilter:
                    if eventpackage.room_id in config.commandFilter[eventpackage.command]:
                        output = self.actuallyRun(eventpackage)
                else:
                    output = self.actuallyRun(eventpackage)
        else:
            output = self.commandList["set"].check(eventpackage);

        return output
