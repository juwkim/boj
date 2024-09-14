import sys
input = lambda: sys.stdin.readline().rstrip()

patern, prev = set(), set()
ans = []

def match(ip1, ip2):
    return any(all(ip1[j] == '.' or ip1[j] == ip2[i + j] for j in range(len(ip1))) for i in range(len(ip2) - len(ip1) + 1))

for _ in range(int(input())):
    s = input()
    if s in prev or s in patern:
        continue
    if any(match(s, ip) for ip in patern):
        prev.add(s)
        ans.append(s)
    else:
        patern.add(s)

print(len(ans))
for ip in ans:
    print(ip)