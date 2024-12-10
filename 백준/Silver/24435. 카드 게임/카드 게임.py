from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    bob, alice = input(), input()
    num = min(int(bob), int(bob[::-1]))
    ans = 0
    for l in permutations(alice):
        cur = int(''.join(l))
        if ans < cur < num:
            ans = cur
    if ans == 0:
        ans = int("".join(sorted(alice, reverse=True)[:-1]))
    print(ans)