t, d, n = map(int, input().split())
traffic_lights = []
for i in range(n):
    a, b, p = map(int, input().split())
    traffic_lights.append((p, a, b))

traffic_lights.sort()

def traffic(velocity: float):
    time = 0
    last_stop = 0
    for i in range(n):
        p, a, b = traffic_lights[i]
        time += (p - last_stop) / velocity
        #print(time)
        wait_time = int(time) % (a + b) + time - int(time)
        if 0 < wait_time <= a:
            time += a - wait_time 
        last_stop = p
        #print(wait_time, time)
    time += (d - last_stop) / velocity
    return time

ERROR = 10 ** (-9)

def binary_search(error_margin=ERROR) -> str:
    minimum = t
    left, right = 0, d
    while right - left >= error_margin:
        mid = (right + left) / 2
        res = traffic(mid)
        if res < d and res < minimum:
            right = mid
        else:
            left = mid
    return left

print(binary_search())