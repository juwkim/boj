while(s:=input())!='#':
    for _ in[0]*len(s):
        if s[0]in'aeiou':break
        else:s=s[1:]+s[0]
    print(s+'ay')