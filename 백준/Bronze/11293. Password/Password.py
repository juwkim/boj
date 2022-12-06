for i in range(1, 1 + int(input())):
    ans = [input().replace(' ', '') for _ in range(int(input()))]
    
    print('Customer', i)
    for _ in range(int(input())):
        *l, x, y = input().split()
        num, a, b = map(lambda x: int(x) - 1, l)
        if ans[num][a] + ans[num][b] == x + y:
            print('correct')
        else:
            print('error')