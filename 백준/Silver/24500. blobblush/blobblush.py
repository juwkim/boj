N = int(input())

if N & N + 1:
    print(2)
    print((1 << N.bit_length()) - N - 1)
    print(N)
else:
    print(1)
    print(N)