N, M, K = map(int, input().split())
print(min(N.bit_length(), K.bit_length() + M) - 1)