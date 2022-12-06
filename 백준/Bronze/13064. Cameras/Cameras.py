for _ in' '*int(input()):
    p=input()
    if p[0]==p[1]and p[4].isupper()and all('0'<i<':'for i in p[:4]+p[5:]):print(p)