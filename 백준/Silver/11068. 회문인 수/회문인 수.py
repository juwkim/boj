alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?'
def change(num, base):
    ans = ''
    while True:
        num, q = divmod(num, base)
        ans = alphabet[q] + ans
        if num == 0:
            break
    return ans

for _ in range(int(input())):
    num = int(input())
    ans = 0
    for base in range(2, 65):
        tmp = change(num, base)
        if tmp == tmp[::-1]:
            ans = 1
            break
    print(ans)