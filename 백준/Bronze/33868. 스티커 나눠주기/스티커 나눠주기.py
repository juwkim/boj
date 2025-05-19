N = int(input())
T, B = zip(*[map(int, input().split()) for _ in range(N)])
print(max(T) * min(B) % 7 + 1)