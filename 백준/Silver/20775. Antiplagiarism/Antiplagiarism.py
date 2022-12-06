N = int(input())
a = [tuple(input()) for _ in range(N)]
input()
b = [tuple(input()) for _ in range(N)]

ans = 'NO'
for i in range(4):
    if a == b:
        ans = 'YES'
        break
    a = [i[::-1] for i in zip(*a)]
if ans == 'NO':
    a = [i[::-1] for i in a]
    for i in range(4):
        if a == b:
            ans = 'YES'
            break
        a = [i[::-1] for i in zip(*a)]
print(ans) 