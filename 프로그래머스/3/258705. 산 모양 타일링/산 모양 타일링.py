def solution(n, tops):
    a, b = 1, 1
    for i in range(2 * n):
        if i & 1 or not tops[i // 2]:
            a, b = b, (a + b) % 10007
        else:
            a, b = b, (a + 2 * b) % 10007
    return b