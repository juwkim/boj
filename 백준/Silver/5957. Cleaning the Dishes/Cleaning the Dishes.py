g = lambda: [*map(int, input().split())]


N = int(input())
bessie = [*range(N, 0, -1)]
canmuu = []
ans = []
while len(ans) != N:
    cmd, amount = g()
    if cmd == 1:
        for _ in range(amount):
            canmuu.append(bessie.pop())
    else:
        for _ in range(amount):
            ans.append(canmuu.pop())
print(*ans[::-1])