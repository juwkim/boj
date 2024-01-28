import sys
input = lambda: sys.stdin.readline().rstrip()

while n:=int(input()):
    buf = []
    for _ in range(n):
        s = input()
        name = [s[0]]
        for a, b in zip(s, s[1:]):
            if a in "aeiou":
                name.append(b)
        buf.append("".join(name))
    ans = -1
    for k in range(1, max(map(len, buf)) + 1):
        if len(set(map(lambda x: x[:k], buf))) == n:
            ans = k
            break
        k += 1
    print(ans)