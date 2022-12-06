com = pow(10, 18)
for _ in range(int(input())):
    N = int(input())
    num = N
    while num <= com and sum(int(i) for i in str(num - N)) & 1 == 0:
        num *= 10
    print(num - N)