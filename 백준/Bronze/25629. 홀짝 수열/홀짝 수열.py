N = int(input())
odd = sum(num&1 for num in map(int, input().split()))
print(int((N + 1) // 2 == odd))    