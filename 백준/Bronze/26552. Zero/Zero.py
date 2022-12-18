for _ in range(int(input())):
    K = int(input()) + 1
    while '0' in str(K):
        K += 1
    print(K)