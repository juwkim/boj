s = input()
Max, Min = [], []
cnt = 0
for c in s:
    if c == 'M':
        cnt += 1
    else:
        Max.append('5')
        for _ in range(cnt):
            Max.append('0')
        if cnt:
            Min.append('1')
            for _ in range(cnt - 1):
                Min.append('0')
        Min.append('5')
        cnt = 0
for _ in range(cnt):
    Max.append('1')
if cnt:
    Min.append('1')
    for _ in range(cnt - 1):
        Min.append('0')
print(*Max, sep='')
print(*Min, sep='')