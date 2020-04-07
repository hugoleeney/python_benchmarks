from time import time


class timer:
    def __init__(self, name="timer"):
        self.name = name
    def __enter__(self):
        print("timing: %s"%self.name)
        self.starttime = time()
        return self
    def __exit__(self, type, value, traceback):
        endtime = time()
        self.total_time = endtime-self.starttime
        print("runtime=%s"%(self.total_time))
