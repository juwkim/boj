for _ in range(3):
    times = [list(map(int, time.split(':'))) for time in input().split(' ')]
    start, end = [time[0] * 3600 + time[1] * 60 + time[2] for time in times]
    count = 0
    while start != end:
        start = int(''.join(map(lambda x: str(x).zfill(2), [start//3600, (start%3600)//60, (start%3600)%60])))
        count += int(start%3 == 0)
        start = str(start).zfill(6)
        h, m, s = map(int, [start[:2], start[2:4], start[4:]])
        start = (h * 3600 + m * 60 + s + 1) % 86400
    end = int(''.join(map(lambda x: str(x).zfill(2), times[1])))
    count += int(end%3 == 0)
    print(count)