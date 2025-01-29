N = int(input())
print(1 + sum(num.bit_length() - 1 for num in sorted(map(int, input().split()))[:N + 1 >> 1]))