buf = []
while True:
    try:
        name, sale, profit = input().split()
        sale = int(sale)
        profit = float(profit)
        buf.append((-sale * profit, -sale, name))
    except:
        break
buf.sort()
for profit, sale, name in buf:
    print(f'${-profit:#.2f} - {name}/{-sale}')