import time

class Timer():
    def __init__(self):
        self.start = None
        self.end = None
        self.time_spent = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        self.time_spent = self.end - self.start

with Timer() as timer:
    time.sleep(0.1)

print(timer.time_spent)
