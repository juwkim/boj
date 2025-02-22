from itertools import permutations
while (p:=input().split())[0] != '0':
    n, *v, m = p
    s = input()
    alpha = [*{ord(c) for c in s if c.isalpha()}]
    ans = "NO"
    for l in permutations(v):
        d = {a: b for a, b in zip(alpha, l)}
        if eval(f"{s.translate(d)} == {m}"):
            ans = "YES"
            break
    print(ans)