from math import isqrt

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    zeros = A.count(0)
    if zeros > 1:
        print("Yes")
        print(0)
        return
    if zeros == 1:
        print("No")
        return
    prod = 1
    for num in A:
        prod *= num
        if abs(prod) > 10**18:
            print("No")
            return
    if prod < 0:
        print("No")
        return
    num = isqrt(prod)
    if num * num == prod:
        if num in A:
            print("Yes")
            print(num)
            return
        elif -num in A:
            print("Yes")
            print(-num)
            return
    print("No")
solve()