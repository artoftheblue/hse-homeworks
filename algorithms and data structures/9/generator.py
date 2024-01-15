from random import randrange

with open(r"algorithms and data structures\9\input.txt", "w") as f:
    n = randrange(100, 1000)
    f.write(str(n)+ "\n")
    for _ in range(n):
        f.write(str(randrange(0, 1000)) + " ")
    f.write("\n")
    
    k = randrange(5, 100)
    f.write(str(k)+"\n")
    
    for _ in range(k):
        l = randrange(1, n)
        r = randrange(l, n)
        f.write(f"{l} {r}\n")