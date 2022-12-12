g = lambda: tuple(map(int, input().split()))
p = ((1, 19), (2, 18), (3, 20), (4, 19), (5, 20), (6, 21), (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (12, 21))
check = bytearray(12)
for _ in range(7):
    day = g()
    idx = sum(day > i for i in p) - 1
    check[idx] = 1
ans = []
for _ in range(int(input())):
    day = g()
    idx = sum(day > i for i in p) - 1
    if check[idx] == 0:
        ans.append(day)
if ans:
    for day in sorted(ans):
        print(*day)
else:
    print("ALL FAILED")