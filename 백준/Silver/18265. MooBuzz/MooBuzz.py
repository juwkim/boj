N = int(input())
def check(x):
    ret = x - x // 3 - x // 5 + x // 15
    return ret
l, r = 1, 1875 * 10**6
while True:
    m = (l + r) // 2
    tmp = check(m)
    if tmp == N:
        break
    elif tmp > N:
        r = m - 1
    else:
        l = m + 1
while m % 3 == 0 or m % 5 == 0:
    m -= 1
print(m)