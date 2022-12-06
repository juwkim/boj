T = int(input())
for _ in range(T):
    total_C, total_G = 0, 0
    N = int(input())
    for _ in range(N):
        C, G = map(float, input().split())
        total_C += C
        total_G += C * G
    print(int(total_C), total_G / total_C)