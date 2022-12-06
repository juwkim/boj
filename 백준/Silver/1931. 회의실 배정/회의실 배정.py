count, num = 0, 0
times = sorted([[*map(int, input().split())] for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
for start, end in times:
    if start >= num:
        num = end
        count += 1
print(count)