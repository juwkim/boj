S, C, O, N = map(int, input().split())
print(min((S + N) // 3, (C + 2 * O) // 6))