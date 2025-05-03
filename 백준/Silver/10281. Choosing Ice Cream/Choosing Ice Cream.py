for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = "unbounded"
    if k > 1:
        prod = 1 % n
        for i in range(30):
            if prod == 0:
                ans = i
                break
            prod = (prod * k) % n
    print(ans)