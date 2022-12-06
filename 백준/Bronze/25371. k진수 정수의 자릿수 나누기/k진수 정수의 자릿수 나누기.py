g = lambda: [*map(int, input().split())]

def change(n, base):
    ans = ''
    while True:
        n, q = divmod(n, base)
        ans = str(q) + ans
        if n == 0:
            break
    return ans

n, k = g()
b = sum(int(i) for i in change(n, k).split('0') if i)
print(change(b, k))