buf = [input() for _ in range(int(input()))]
buf.sort(key=lambda x: (len(x), x))
print(*buf)