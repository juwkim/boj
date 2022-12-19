g = lambda: [*map(int, input().split())]
dic = {}
while sum(S:= g()):
    X, Y = S
    for num in (X, Y, -X, -Y, X - Y):
        if num not in dic:
            if num >= 0:
                dic[num] = bin(num)[2:].zfill(8)
            else:
                dic[num] = '1' + bin(num + 128)[2:].zfill(7)
        print(f'{num} = {dic[num]}')
    print()