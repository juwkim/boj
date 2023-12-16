import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

tc = 1
while n := int(input()):
    x = [int(l[1:]) - 1 for l in input().split()]
    terminal = input()
    ans = []
    for _ in range(int(input())):
        VVA = input()
        l, r = 0, 2**n - 1
        for i in x:
            if VVA[i] == "0":
                r = (l + r) // 2
            else:
                l = (l + r) // 2 + 1
        ans.append(terminal[l])    
    print(f"S-Tree #{tc}:")
    print(*ans, sep="")
    print()
    tc += 1