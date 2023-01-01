def check(a, op, b, c, base):
    
    if base == 1:
        p = a.count('1')
        q = b.count('1')
        r = c.count('1')
    else:    
        p = int(a, base)
        q = int(b, base)
        r = int(c, base)
    if any(num > INT_MAX for num in [p, q, r]):
        return False
    return eval(f'{p} {op} {q} == {r}')

INT_MAX = (1 << 32) - 1
dic = {'0': 2, '1': 1, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, 'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16, 'g': 17, 'h': 18, 'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23, 'n': 24, 'o': 25, 'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30, 'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36}
to_base = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: '0'}

for _ in range(int(input())):
    s = input()
    Min_base = 1
    for c in s:
        if c in dic:
            Min_base = max(Min_base, dic[c])
            
    ans = []
    a, op, b, _, c = s.split()
    for base in range(Min_base, 37):
        if check(a, op, b, c, base):
            ans.append(to_base[base])
    if ans:
        print(*ans, sep='')
    else:
        print('invalid')