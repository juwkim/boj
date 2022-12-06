def to_decimal(s):
    if '0' <= s <= '9':
        return ord(s) - 48
    elif 'A' <= s <= 'Z':
        return ord(s) - 55
    else:
        return ord(s) - 61

def to_base(n):
    if 0 <= n <= 9:
        return chr(n + 48)
    elif 10 <= n <= 35:
        return chr(n + 55)
    else:
        return chr(n + 61)

for _ in [0]*int(input()):
    base_from, base_to, n = input().split()
    base_from, base_to = map(int, [base_from, base_to])
    num = sum(to_decimal(n[i]) * pow(base_from, -i-1) for i in range(-1, -len(n)-1, -1))
    a = ''
    while num:
        a = to_base(num % base_to) + a
        num //= base_to
    print(f'{base_from} {n}\n{base_to} {a or 0}\n')