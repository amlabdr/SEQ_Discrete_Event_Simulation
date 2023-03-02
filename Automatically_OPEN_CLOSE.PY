from sequence.kernel.timeline import Timeline
from sequence.kernel.event import Event
from sequence.kernel.process import Process

class Store(object):
    def __init__(self, tl: Timeline):
        self.open = False
        self.timeline = tl

    def openSTORE(self) -> None:    
        if self.timeline.now() >= 60:
            self.timeline.stop()
        self.open = True
        process = Process(self, 'closeSTORE', [])
        event = Event(self.timeline.now() + 12, process)
        self.timeline.schedule(event)

    def closeSTORE(self) -> None:
        if self.timeline.now() >= 60:
            self.timeline.stop()
        self.open = False
        process = Process(self, 'openSTORE', [])
        event = Event(self.timeline.now() + 12, process)
        self.timeline.schedule(event)


for t in [15, 32, 52]:
    tl = Timeline(t)
    store = Store(tl)
    print(tl.now())
    
    process = Process(store, 'openSTORE', [])
    event = Event(7, process)
    tl.schedule(event)
    
    tl.run()
    print(store.open)
# True, True, False