c,i=[0]*int(input()),0
for w in input().split():
    c[i]+=(w[0].isupper()and all(96<ord(s)<123 or ord(s)in[33,46,63]for s in w[1:]))
    i+=(w[-1]in'.?!')
print(*c)