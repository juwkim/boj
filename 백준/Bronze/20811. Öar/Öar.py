root5 = 5**.5
a, b = (1 + root5) / 2, (1 - root5) / 2

def fibo(n):
    global a, b, root5
    return round((a**n - b**n) / root5)

n = int(input())
i = 1
while fibo(i) <= n:
    i += 1
print(i - 2)