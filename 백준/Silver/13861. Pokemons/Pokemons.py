f = open(0)
def read():
    num = ''
    while True:
        ch = f.read(1)
        if ch.isspace():
            yield float(num)
            num = ''
        else:
            num += ch
tokens = read()
money = next(tokens)
n = int(next(tokens))
min_price, max_ratio = next(tokens), -1e18
for _ in range(n - 1):
    price = next(tokens)
    max_ratio = max(max_ratio, price / min_price)
    min_price = min(min_price, price)
print(f"{(max_ratio - 1) * money + 1e-8:.2f}")