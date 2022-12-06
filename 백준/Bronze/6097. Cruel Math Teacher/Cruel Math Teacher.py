s=str(eval(input().replace(' ','**')))
print(*[s[i:i+70]for i in range(0,len(s),70)])