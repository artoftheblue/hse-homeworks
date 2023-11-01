import sys

class ZeroDivisionHandler():
    def __init__(self):
        pass
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type == ZeroDivisionError:
            print(exc_value)
            return True

with ZeroDivisionHandler():
    print(1/0)
    print(1)

with ZeroDivisionHandler():
    print(25)
    print(1/0)
