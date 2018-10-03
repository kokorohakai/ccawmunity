from ..command import Command
from ..eventpackage import EventPackage
import urllib
import random
import time
from html.parser import HTMLParser

class RimgCommand(Command):
    def __init__(self):
        self.name = "rimg"
        self.help = "1. search parameters. returns a random image with search parameters."
        self.author = "skuld"
        self.last_updated = "Sept. 28, 2018"

    def run(self, event_pack: EventPackage):
        random.seed(time.time())

        #prepare the search terms
        searchTerms = event_pack.body
        searchTerms.pop(0)
        search = "sfw+"+"+".join(searchTerms)
        url = "https://www.google.com/search?tbm=isch&q="+search+"&oq="+search+"&gs_l=img&safesearch=on"

        #get the page
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req)
        text = response.read()

        #html parser
        parser = HTMLParser()
        theImages = []
        def handleTag(tag, attrs):
            if tag == "img":
                for n in attrs:
                    if n[0] == "data-src":
                        #print(n[1])
                        theImages.append(str(n[1]))

        parser.handle_starttag = handleTag
        parser.feed(str(text))

        nrimg = random.randint(0,len(theImages))

        return theImages[nrimg]
