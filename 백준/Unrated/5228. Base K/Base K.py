def change(n, k):
    ans = ''
    while True:
        ans = '0123456789abcdef'[n%k] + ans
        n //= k
        if n == 0:
            break
    return ans

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = change(n, k)
    p = all(i in s for i in '0123456789abcdef'[:k])
    if p:
        print(f'Base-{k} representation of {n} is {s}; contains all digits.')
    else:
        print(f'Base-{k} representation of {n} is {s}; does not contain all digits.')