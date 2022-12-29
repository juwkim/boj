for _ in range(int(input())):
    input()
    print(sum(sorted(map(int, input().split()), reverse=True)[2::3]))