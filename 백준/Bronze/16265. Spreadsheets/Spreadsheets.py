for _ in[0]*int(input()):
    n,s=int(input()),''
    while n:s=chr((n-1)%26+65)+s;n=(n-1)//26
    print(s)