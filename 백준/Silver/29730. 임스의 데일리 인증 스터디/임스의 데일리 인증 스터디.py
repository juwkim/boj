import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

boj, study = [], []
for _ in range(int(input())):
    s = input()
    if s.startswith("boj.kr/"):
        boj.append(int(s[7:]))
    else:
        study.append(s)
for l in sorted(study, key=lambda x: (len(x), x)):
    print(l)
for num in sorted(boj):
    print(f"boj.kr/{num}")