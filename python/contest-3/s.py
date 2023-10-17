from math import gcd 
 
def ReduceFraction(n, m) :
    d = gcd(n, m);
    p = n // d;
    q = m // d;
    return (p, q)

print(*ReduceFraction(int(input()), int(input())))
