for _ in range(3):
    h0, m0, s0, h1, m1, s1 = list(map(int, input().split()))
    second = (h1 - h0) * 3600 + (m1 - m0) * 60 + s1 -s0
    print(second // 3600, (second % 3600) // 60, second % 60)