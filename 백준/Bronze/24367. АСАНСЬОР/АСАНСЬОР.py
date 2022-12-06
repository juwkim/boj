from itertools import combinations
M, N = map(int, input().split())
t1, t2, t3, t4 = sorted(map(int, input().split()))
a = sum([t1, t2, t3, t4])

if t1 >= N:
    print(4)
elif a <= N:
    print(1 + (M < 4))
elif M >= 3:
    if sum([t1, t2, t3]) <= N or t2 + t4 <= N or (t1 + t4 <= N and t2 + t3 <= N):
        print(2)
    elif all(a + b > N for a, b in combinations([t1, t2, t3, t4], 2)):
        print(4)
    else:
        print(3)
else:
    if t2 + t4 <= N or (t1 + t4 <= N and t2 + t3 <= N):
        print(2)
    elif all(a + b > N for a, b in combinations([t1, t2, t3, t4], 2)):
        print(4)
    else:
        print(3)