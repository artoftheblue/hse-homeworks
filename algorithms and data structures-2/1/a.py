string = input()
substring = input()

def custom_hash(data):
    hash_ = 0
    for i in range(len(data) -1, -1, -1):
        hash_ += ord(data[i])