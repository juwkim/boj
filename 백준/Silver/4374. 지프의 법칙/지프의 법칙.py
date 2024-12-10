from collections import Counter

l = [*open(0)][::-1]
while l:
    n = int(l.pop())
    cnt = Counter()
    while (s:=l.pop()) != "EndOfText\n":
        cur = []
        for c in s.lower():
            if c.isalpha():
                cur.append(c)
            elif cur:
                cnt["".join(cur)] += 1
                cur = []
    ans = sorted(k for k, v in cnt.items() if v == n)
    if ans: print(*ans, sep="\n")
    else: print("There is no such word.")
    print()