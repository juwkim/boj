import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    buf = input().split()
    ans = []
    Set = set()
    while (s := input()) != 'what does the fox say?':
        Set.add(s.split()[2])
    for s in buf:
        if s not in Set:
            ans.append(s)
    print(*ans)