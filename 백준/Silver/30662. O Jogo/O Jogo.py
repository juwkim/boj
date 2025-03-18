# import sys
# # input = sys.stdin.readline
# from collections import defaultdict

# f = open("python/a.in", "r")
# g = open("python/a.out", "r")
# input = lambda: f.readline().rstrip()
# check = lambda: g.readline().rstrip()
# tc = 1
# while n:=int(input()):
#     dic = defaultdict(set)
#     res = defaultdict(set)
#     keys = set()
#     for _ in range(n):
#         day, cmd, A, *B = input().split()
#         match cmd[0]:
#             case 'S':
#                 A, B = A[:-1], B[0]
#                 keys.update((A, B))
#                 dic[B].add(A)
#             case 'U':
#                 A, B = A[:-1], B[0]
#                 keys.update((A, B))
#                 dic[B].remove(A)
#             case 'P':
#                 keys.add(A)
#                 visited = {A}
#                 st = [A]
#                 while st:
#                     a = st.pop()
#                     for b in dic[a]:
#                         if b not in visited:
#                             visited.add(b)
#                             st.append(b)
#                 for name in visited:
#                     res[name].add(day)
#     num = min(len(res[k]) for k in keys)
#     ans = [k for k in keys if len(res[k]) == num]
#     s, t = " ".join(sorted(ans)), check()
#     if s == t:
#         tc += 1
#     else:
#         print(tc, len(s.split()), len(t.split()))
#         print(s)
#         print()
#         print(t)
#         exit(0)

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
    print(*sorted(k for k in keys if len(res[k]) == num))