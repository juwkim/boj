k1, v1 = input().split()

front, back = {}, {}
for _ in range(2):
    k, v = input().split()
    front[k] = v

for _ in range(2):
    k, v = input().split()
    back[k] = v

k2, v2 = input().split()
    

while (l:= input()) != '-1':
    ans = 0
    if l == k1:
        ans += int(v1)
    if l[4:] == k2:
        ans += int(v2)
    if front.get(l[:3]):
        ans += int(front.get(l[:3]))
    if back.get(l[3:]):
        ans += int(back.get(l[3:]))
    print(ans)