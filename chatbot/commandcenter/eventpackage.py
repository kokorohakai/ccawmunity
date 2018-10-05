class EventPackage():
    def __init__(self, body={}, room_id="", sender="", event={}, command="", prefix=""):
        self.body = body
        self.room_id = room_id
        self.sender = sender
        self.event = event
        self.commmand = command
