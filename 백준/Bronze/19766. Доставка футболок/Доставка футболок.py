def g():
    return map(int, input().split())

n, k, t = g()
moves, home_times = [*g()], [*g()]
total_time = 0

for i in range(n):
    total_time += moves[i]
    if total_time >= home_times[i]:
        total_time += t
    elif total_time + k >= home_times[i]:
        total_time += home_times[i] - total_time + t
    else:
        total_time += k

print(total_time)