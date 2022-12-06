g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n, k = g()
    me = input()
    ancestor = [input() for _ in range(n)]
    ans = 0
    for i in range(k):
        ans += all(me[i] != other[i] for other in ancestor)
    print(f'Data Set {cnt}:\n{ans}/{k}\n')