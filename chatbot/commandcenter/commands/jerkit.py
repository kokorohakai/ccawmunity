from ..command import Command
from ..eventpackage import EventPackage
import bot
import requests
import json
import ast
import random

class JerkitCommand(Command):
    def __init__(self):
        self.name = "jerkit"
        self.help = "retrieves some random nonsense from bonequest.com"
        self.author = "Skuld"
        self.last_updated = "Oct. 3rd, 2018"

    def run(self, event_pack: EventPackage):
        url = "https://www.bonequest.com/api/v2/quote/random/1"
        data = requests.get(url).json()
        dialog = data["episodes"][0]["dialog"]
        n = 0;

        output = ""
        for q in dialog:
            output += q[0]
            if len(q) > 0:
                output += ": " + q[1]
            output += "\n"
        return output
