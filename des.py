from sequence.kernel.timeline import Timeline

class Store(object):
    def __init__(self, tl: Timeline):
        self.open = False
        self.timeline = tl

    def openStore(self) -> None:
        self.open = True

    def closeStore(self) -> None:
        self.open = False

from sequence.kernel.event import Event
from sequence.kernel.process import Process

tl = Timeline() # create timeline
tl.show_progress = False # turn of progress bar, we will address this in later tutorials.
store = Store(tl) # create store

# open store at 7:00
open_proc = Process(store, 'openStore', []) # Process(object, function name: string, arguments of function: List[])
open_event = Event(7, open_proc) # Event(occurring time: int, process: Process)
tl.schedule(open_event) # Timeline.schedule(Event)
print("Before Running",store.open)

tl.run()
print(tl.now(), store.open) # 7 True

close_proc = Process(store, 'closeStore', [])
close_event = Event(19, close_proc)
tl.schedule(close_event)
tl.run()
print(tl.time, store.open) # 19 False

tl.time = 0
tl.schedule(open_event)
tl.schedule(close_event)
tl.run()
print(tl.time, store.open)

tl.time = 0
tl.schedule(close_event)
tl.schedule(open_event)
tl.run()
print(tl.time, store.open)