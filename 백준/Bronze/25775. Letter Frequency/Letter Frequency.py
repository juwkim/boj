from statistics import multimode

n = int(input())
s = [input() for _ in range(n)]
for i in range(1, 1 + len(max(s, key=len))):
    a = []
    for j in range(n):
        if len(s[j]) >= i:
            a.append(s[j][i-1])
    print(f'{i}:', *sorted(multimode(a)))