while True:
    start, period = [list(map(int, i.split(':'))) for i in input().split()]
    if [start, period] == [[0, 0], [0, 0]]:
        break
    time = (start[0] + period[0]) * 60 + start[1] + period[1]
    day, hour, minute = time//1440, time%1440//60, time%1440%60
    end = ':'.join(map(lambda x: str(x).zfill(2), [hour, minute]))
    print(end, f'+{day}' if day else '')