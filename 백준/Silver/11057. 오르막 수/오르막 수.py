mod = 10007
buf = [1] * 10
for _ in range(int(input()) - 1):
    num = 0
    buf = [num := (num + buf[i]) % mod for i in range(10)]
print(sum(buf) % mod)