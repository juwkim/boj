import sys
input = sys.stdin.readline
from collections import defaultdict

while n:=int(input()):
    dic = defaultdict(set)
    res = defaultdict(set)
    keys = set()
    for _ in range(n):
        day, cmd, A, *B = input().split()
        match cmd[0]:
            case 'S':
                A, B = A[:-1], B[0]
                keys.update((A, B))
                dic[B].add(A)
            case 'U':
                A, B = A[:-1], B[0]
                keys.update((A, B))
                dic[B].remove(A)
            case 'P':
                res[A].add(day)
                for name in dic[A]:
                    res[name].add(day)
    num = min(len(res[k]) for k in keys)
    ans = [k for k in keys if len(res[k]) == num]
    print(*sorted(ans))