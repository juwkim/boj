N = int(input())
lines = [input() for _ in range(N)]
ans = []
for l in zip(*lines):
    if len(set(l)) == 1:
        ans.append(l[0])
    else:
        ans.append('?')
print(''.join(ans))