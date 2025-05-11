import sys

def token_stream():
    num = ''
    while True:
        ch = sys.stdin.read(1)
        if not ch:
            if num:
                yield float(num)
            break
        if ch.isspace():
            if num:
                yield float(num)
                num = ''
        else:
            num += ch

tokens = token_stream()
money = next(tokens)
n = int(next(tokens))
min_price = next(tokens)

max_ratio = -1e18

for _ in range(n - 1):
    price = next(tokens)
    if price > max_ratio * min_price:
        max_ratio = price / min_price
    if price < min_price:
        min_price = price

profit = (max_ratio - 1) * money + 1e-8
print(f"{profit:.2f}")
