n, p, m = map(int, input().split())
dic = {input(): 0 for _ in range(n)}
buf = []
for _ in range(m):
    name, score = input().split()
    dic[name] += int(score)
    if dic[name] >= p:
        buf.append(name + ' wins!')
        dic[name] = -1e9
if buf:
    print(*buf, sep='\n')
else:
    print('No winner!')