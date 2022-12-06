N = int(input())
buf = [input() for _ in range(N)]
for k in range(1, 1 + len(buf[0])):
    if len(set(student[-k:] for student in buf)) == N:
        print(k)
        break