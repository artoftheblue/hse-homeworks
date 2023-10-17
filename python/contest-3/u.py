def fhib(n):
    fhib.counter += 1
    if n == 1 or n == 2:
        return 1
    return fhib(n - 1) + fhib(n - 2)
fhib.counter = 0
fhib(int(input()))
print(fhib.counter)
