table = {'m': 1000, 'c': 100, 'x': 10, 'i': 1}
def decode_mcxi(s):
    num = 0
    tmp = None
    for c in s:
        if c in table:
            if tmp:
                num += tmp * table[c]
                tmp = None
            else:
                num += table[c]
        else:
            tmp = int(c)
    return num

def encode_mcxi(num):
    mcxi = ""
    for c in 'ixcm':
        if num == 0:
            break
        num, q = divmod(num, 10)
        if q == 0:
            continue
        if q == 1:
            mcxi = c + mcxi
        else:
            mcxi = f'{q}{c}' + mcxi
    return mcxi

for _ in range(int(input())):
    num = sum(map(decode_mcxi, input().split()))
    mcxi = encode_mcxi(num)
    print(mcxi)