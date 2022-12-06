a='TTT TTH THT THH HTT HTH HHT HHH'.split()
for _ in[0]*int(input()):
    s=input()
    print(*[[s[i:i+3]for i in range(len(s)-2)].count(i) for i in a])