for _ in range(int(input())):
    M, N = input().split()
    if M == '1':
        a = sum(int(num) << (56 - 8 * idx) for idx, num in enumerate(N.split('.')))
        print(a)
    else:
        buf = []
        N = int(N)
        for _ in range(8):
            buf = [N % 256] + buf
            N //= 256
        print(*buf, sep='.')