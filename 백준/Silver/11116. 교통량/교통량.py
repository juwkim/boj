g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    m = int(input())
    left = g()
    right = g()
    s_left = set(left)
    s_right = set(right)
    
    ans = 0
    for i in range(m):
        tmp = left[i]
        if tmp + 500 in s_left and tmp - 500 not in s_right:
            ans += 1
            s_left.remove(tmp + 500)
            s_right.remove(tmp + 1000)
            s_right.remove(tmp + 1500)
    print(ans)