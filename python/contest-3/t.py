def fhib(n):
    if n == 1 or n == 2:
        return 1
    return fhib(n - 1) + fhib(n - 2)
print(fhib(int(input())))
