discount = {'R': 0.55, 'G': 0.70, 'B': 0.80,
         'Y': 0.85, 'O': 0.90, 'W': 0.95}

from math import floor
for _ in [0] * int(input()):
    original_price, dot, coupon, payment = input().split()
    price = float(original_price) * discount[dot] * (1 - 0.05 * (coupon == 'C'))
    if payment == 'C':
        print(f'${round(price - 0.00999999999, 1):#.2f}')
    else:
        print(f'${price:#.2f}')