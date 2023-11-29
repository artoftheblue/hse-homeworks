from random import randint

def enough_balloons_for_given_time(time) -> tuple[bool, list[int]]:
    global helpers, balloon_target

    balloons_at_all = 0
    balloons_per_helper = [0 for _ in range(len(helpers))]

    enough_flag = False

    for h_i in range(len(helpers)):
        t, z, y = helpers[h_i]
        balloons_filled = 0

        # full_cycles, time_left = divmod(time, (z * t + y))
        # balloons_filled += z * full_cycles
        time_left = time

        left_before_rest = z
        while time_left - t >= 0:
            if balloons_at_all >= balloon_target:
                enough_flag = True
                break
            if left_before_rest == 0:
                time_left -= y
                left_before_rest = z
                continue
            time_left -= t
            balloons_filled += 1
            balloons_at_all += 1
            left_before_rest -= 1
        balloons_per_helper[h_i] = balloons_filled

        if enough_flag:
            break

    return balloons_at_all >= balloon_target, balloons_per_helper


balloon_target, n_helper = randint(50, 100), randint(10, 100)
print(balloon_target, n_helper)

helpers = []
for i in range(n_helper):
    src = (randint(1, 10), randint(1, 10), randint(1, 10))  # t, z, y
    print(*src)
    helpers.append(src)

# left bin search

left = -1
right = 10 ** 9

last_good = []

while right - left > 1:
    mid = (right + left) // 2
    can_be_done, per_guy = enough_balloons_for_given_time(mid)
    if can_be_done:
        right = mid
        last_good = per_guy
    else:
        left = mid

print(right)
print(' '.join(str(x) for x in last_good))