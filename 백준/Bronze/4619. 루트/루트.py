import math
while True:
    B, N = map(int, input().split())
    if (B, N) == (0, 0):
        break
    A = math.exp(1)**(math.log(B)/N)
    print([int(A), math.ceil(A)][int(A)**N + math.ceil(A)**N < 2*B])