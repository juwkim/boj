g = lambda s: (s in 'SZ') + 2 * (s == 'Z') + (ord(s) + (s < 'S'))%3 + 1
def check(s, last):
    if any(i == ' ' for i in [s, last]):
        return False
    elif s < 'P' and last < 'P':
        return (ord(s)+1)//3 == (ord(last)+1)//3
    elif s < 'T':
        return all(i in 'PQRS' for i in [s, last]) 
    elif s < 'W':
        return all(i in 'TUV' for i in [s, last])
    else:
        return all(i in 'WXYZ' for i in [s, last])
    
p, w = map(int, input().split())
s = input()
print(g(s[0])*p + sum(g(b) * p + check(a, b) * w for a, b in zip(s, s[1:])))