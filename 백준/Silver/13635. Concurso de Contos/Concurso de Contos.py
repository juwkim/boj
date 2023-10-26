import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    try:
        N, L, C = map(int, input().split())
        line, char = 0, 0
        for word in input().split():
            if char + len(word) <= C:
                char += len(word) + 1
            else:
                line += 1
                char = len(word) + 1
        ans = line // L + 1
        print(ans)
    except:
        break