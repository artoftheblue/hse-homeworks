from collections import Counter, defaultdict
from math import inf
from copy import copy


from random import sample, randrange

for i in range(100):
INFINITY = 1000000000000000000

def ATM(n: int, banknotes: list, s: int):
    array = [INFINITY] * (s + 1)
    array[0] = 0
    for i in range(1, s + 1):
        for banknote in banknotes:
            if i >= banknote and array[i - banknote] + 1 < array[i]:
                array[i] = array[i - banknote] + 1
    
    #print(array)
    if array[s] == INFINITY:
        print(-1)
    else:
        print(array[-1])
        while s > 0:
            for banknote in banknotes:
                if s < banknote:
                    continue
                if array[s - banknote] == array[s] - 1:
                    print(banknote, end=" ")
                    s -= banknote
                    break
        
    n = randrange(5, 10)
    notes = sorted(sample(range(1, 100), n), reverse=True)
    su = randrange(1, 500)
    print("\nDATA:\n----\n", n, notes, su, "\n-----")

    print(ATM(n, notes, su))

    best = defaultdict(lambda: inf)
    combos = defaultdict(lambda: Counter())

    for note in notes:
        summ = 0
        counter = 0
        while summ+note <= su:
            summ += note
            counter += 1
            if best[summ] > counter:
                best[summ] = counter
                combos[summ] = Counter({note: counter})

        for i in range(1, su):
            if i in best and i+note <= su:
                if best[i+note] > best[i]+1:
                    best[i + note] = best[i] + 1
                    combos[i + note] = copy(combos[i])
                    combos[i + note][note] += 1
    if best[su] is inf:
        print(-1)
    else:
        print(best[su])
        print(' '.join(' '.join(str(x) for y in range(combos[su][x])) for x in combos[su]))