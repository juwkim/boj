for _ in range(int(input())):
    ans = 1
    for i in range(3, int(input()), 2):
        ans = ans * i % 1000
    print(ans)