from multiprocessing.dummy import Process
from event_stream import EventStream


class ProcessLauncher:
    def __init__(self):
        p = Process(target=self.run, args=())
        p.daemon = True
        p.start()

    def run(self):
        event_stream = EventStream()
        event_stream.watch()
