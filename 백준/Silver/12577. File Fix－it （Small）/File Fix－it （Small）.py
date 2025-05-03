import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    dirs = set()
    for _ in range(N):
        path = ""
        parts = input().split('/')
        for i in range(1, len(parts)):
            path += '/' + parts[i]
            dirs.add(path)
    cnt = 0
    for _ in range(M):
        path = ''
        parts = input().split('/')
        for i in range(1, len(parts)):
            path += '/' + parts[i]
            if path not in dirs:
                dirs.add(path)
                cnt += 1
    print(f"Case #{tc}: {cnt}")