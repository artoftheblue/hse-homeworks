n = int(input())
jars = list(map(int, input().split()))
jars.sort()

if len(jars) == 1:
    print(0)
else:
    max_diff = 0
    min_length = 0
    z = 0
    for i in range(n - 1):
        if jars[i + 1] - jars[i] > max_diff:
            max_diff = jars[i + 1] - jars[i]
            z = i

    #print(f"[0, {z}] [{z + 1}, {n - 1}]")
    total = 0
    #print(z)
    for a, b in [(0, z), (z + 1, n - 1)]:
        m = jars[b]
        for i in range(a, b + 1):
            total += m - jars[i]
            jars[i] = m
        
        #print(jars)
        if len(set(jars)) == 2:
            break
        
    print(min(total, totalb))