from itertools import accumulate

data = input().split()
a = accumulate([word + " " for word in data])
for i in range(len(data)):
    print(next(a))
