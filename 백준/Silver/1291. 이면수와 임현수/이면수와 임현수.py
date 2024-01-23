import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def factorize(n):
    i = 2
    nums = set()
    while n != 1:
        if n % i == 0:
            nums.add(i)
            n //= i
        else:
            i += 1
    return sorted(nums)

S = input()
N = int(S)
a = (N >= 4 and N != 5 and sum(int(i) for i in S) & 1)
b = (N == 2 or N == 4 or (N != 1 and len(factorize(N)) % 2 == 0))

if a and b:
    print(4)
elif a:
    print(1)
elif b:
    print(2)
else:
    print(3)