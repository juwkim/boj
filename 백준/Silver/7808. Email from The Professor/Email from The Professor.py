l = open(0).readlines()
for i in range(0, len(l), 2):
    p = l[i].rstrip()
    k, *key = map(int, l[i + 1].split())
    s = p + "ㅋ" * (k - (len(p) - 1) % k - 1)
    table = list(map(lambda x: "".join(x).rstrip('ㅋ'), zip(*[s[i:i+k] for i in range(0, len(s), k)])))
    idx = {num: i for i, num in enumerate(key)}
    ans = "".join(table[idx[i]] for i in range(1, k + 1))
    print(ans)