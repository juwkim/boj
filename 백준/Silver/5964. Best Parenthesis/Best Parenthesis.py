import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
st = [[] for _ in range(N//2 + 1)]
d = 0
for _ in range(N):
    if input() == '0':
        d += 1
    else:
        if st[d]:
            st[d-1].append(2 * sum(st[d]) % 12345678910)
            st[d] = []
        else:
            st[d-1].append(1)
        d -= 1
print(sum(st[0]) % 12345678910)