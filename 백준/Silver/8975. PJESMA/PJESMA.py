N = int(input())
Set = {input() for _ in range(N)}
K = (N + 1) // 2

for i in range(1, 1 + int(input())):
    s = input()
    if s in Set:
        K -= 1
        Set.remove(s)
        if K == 0:
            print(i)
            break