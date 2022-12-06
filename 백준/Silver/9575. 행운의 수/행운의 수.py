g = lambda: {*map(int, input().split())}
for _ in range(int(input())):
    input()
    A = g()
    input()
    B = g()
    input()
    C = g()
    ans = set()
    for a in A:
        for b in B:
            for c in C:
                num = str(a + b + c)
                if set(num).issubset({'5', '8'}):
                    ans.add(num)
    print(len(ans))