ans = []
cnt, num = 0, 1

def check(num):
    buf = bytearray(10)
    while num:
        num, r = divmod(num, 10)
        if buf[r]:
            return 0
        buf[r] = 1
    return 1

while cnt != 1000000:
    if check(num):
        cnt += 1
        ans.append(num)
    num += 1

while n:= int(input()):
    print(ans[n-1])