for _ in range(int(input())):
    N = int(input())
    stock = [max(map(int, input().split())) for _ in range(N)]
    print(sum(filter(lambda x: x>0, stock)))