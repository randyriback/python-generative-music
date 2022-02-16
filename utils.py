from time import time, sleep

class LFO:
    def __init__(self, f, min=1, max=127):
        self.current = min
        self.direction = 1
        self.f = f
        self.min = min
        self.max = max

    def step(self):
        self.f(self.current)
        self.current += self.direction   
        if self.current == self.max:
            self.direction = -1 
        elif self.current == self.min:
            self.direction = 1

class Switch_on:
    def __init__(self, f, time_limit=20):
        self.f = f
        self.time_limit = time_limit

    def toggle_on(self):
        start = time() 
        elapsed = 0
        if elapsed > self.time_limit: 
            self.f(0)
            elapsed = time() - start
            sleep(.001)
        else:
            self.f(127)
            elapsed = time() - start  
            sleep(.001)          

def loop(f, time_limit=20):
    start = time()
    elapsed = 0
    while elapsed < time_limit:
        f()
        elapsed = time() - start 
