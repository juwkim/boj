import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, c = sorted(map(int, input().split()))
    if r == c:
        print("dohoon")
    else:
        print(f"jinseo\n{r} {r}")