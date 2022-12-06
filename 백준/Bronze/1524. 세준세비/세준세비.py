for _ in range(int(input())):
    input()
    input()
    S = max(map(int, input().split()))
    B = max(map(int, input().split()))
    print('SB'[S < B])