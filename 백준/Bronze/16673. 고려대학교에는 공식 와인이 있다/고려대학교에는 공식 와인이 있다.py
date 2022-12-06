C, K, P = map(int, input().split())
print(C * (C + 1) * (3 *K + P * (2 * C + 1)) // 6)