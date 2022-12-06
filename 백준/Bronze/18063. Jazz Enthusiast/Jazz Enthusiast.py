n, c = map(int, input().split())
times = [list(map(int, input().split(':'))) for _ in range(n)]
sec = sum(time[0]*60 + time[1] for time in times) - c*(n-1)
print(':'.join(map(lambda x: str(x).zfill(2), [sec//3600, sec%3600//60, sec%3600%60])))