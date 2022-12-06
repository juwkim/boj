for _ in range(int(input())):
    a = input().split()[1:]  
    ans, cur = 0, 0
    for i in a:
        if i == 'O':
            ans = max(ans, cur)
            cur = 0
        else:
            cur += 1
    ans = max(ans, cur)
    print("The longest contiguous subsequence of X's is of length", ans)