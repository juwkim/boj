from itertools import permutations

for tc in range(1, 1 + int(input())):
    s = input()
    ans = set()
    for p in permutations(s):
        l = int("".join(p))
        if l % 7 == 0: ans.add(l)
    print(f"Case {tc}: {len(ans)}")