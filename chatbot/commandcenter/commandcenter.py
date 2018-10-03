import sys
import inspect
import commandcenter.commands
from commandcenter.eventpackage import *

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

    def run(self, eventpackage: EventPackage):
        output = ""
        if eventpackage.command in self.commandList:
            try:
                output = self.commandList[eventpackage.command].run(eventpackage)
            except Exception as e:
                print(e)
                output = "This command failed to execute"
        return output