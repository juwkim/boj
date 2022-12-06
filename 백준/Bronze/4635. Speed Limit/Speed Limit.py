while True:
    n = int(input())
    if n == -1:
        break
    last_time, distance = 0, 0
    for _ in range(n):
        s, t = map(int, input().split())
        distance += s * (t - last_time)
        last_time = t
    print(distance, 'miles')