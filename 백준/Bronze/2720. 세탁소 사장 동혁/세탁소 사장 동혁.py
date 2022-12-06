T = int(input())
for _ in range(T):
    C = int(input())
    print(C // 25, (C % 25) // 10, ((C % 25) % 10) // 5, C % 5)