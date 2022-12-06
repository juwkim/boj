def Round(num, pos):
    s = pow(10, -pos)
    
    if str(num)[pos] < '5':
        num = num // s * s
    else:
        num = (num // s + 1) * s
    
    return num

N = int(input())

num, pos = 10, -1
while N > num:
    N = Round(N, pos)
    num *= 10
    pos -= 1
print(N)