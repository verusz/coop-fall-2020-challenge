
class Event():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.redoEvents = []
        self.events = []

    def add(self, num: int):
        self.value += num
        self.events.append(Event("add", num))
        

    def subtract(self, num: int):
        self.value -= num
        self.events.append(Event("subtract", num))
        

    def undo(self):
        if (self.events):
            last = self.events.pop()
            self.undoAction(last)
            self.redoEvents.append(last)
        

    def redo(self):
        if (self.redoEvents):
            first = self.redoEvents.pop(0)
            self.redoAction(first)
            self.events.append(first)
        

    def bulk_undo(self, steps: int):
        i = 0
        while (self.events and i < steps):
            event = self.events.pop()
            self.undoAction(event)
            self.redoEvents.append(event)
            i += 1

    def bulk_redo(self, steps: int):
        i = 0
        while (self.redoEvents and i < steps): 
            event = self.redoEvents.pop(0)
            self.redoAction(event)
            self.events.append(event)
            i += 1


    def undoAction(self, event: Event):# reverse action if undo
        if event.name == "subtract":
            self.value += event.value
        if event.name == "add":
            self.value -= event.value

    def redoAction(self, event: Event):
        if event.name == "add":
            self.value += event.value
        if event.name == "subtract":
            self.value -= event.value


