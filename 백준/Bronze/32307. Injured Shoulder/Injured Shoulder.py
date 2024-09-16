n = int(input())
s = {input() for _ in range(n)}
ss = set()
for a in s:
    for b in s:
        ss.add(a + b)
        ss.add(b + a)
for _ in range(int(input())):
    word = input()
    ans = 0
    if word in s:
        ans = 1
    elif word in ss:
        ans = 2
    print(ans)