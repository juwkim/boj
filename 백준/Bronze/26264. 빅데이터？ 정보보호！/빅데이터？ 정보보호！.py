N = int(input())
s = input().count('s')
b = N - s
if s == b:
    print('bigdata? security!')
elif s > b:
    print('security!')
else:
    print('bigdata?')