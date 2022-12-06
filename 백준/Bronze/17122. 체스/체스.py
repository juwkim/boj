for _ in [0]*int(input()):
    a,b=input().split()
    print('YNEOS'[(ord(a[0])+int(a[1])+sum(divmod(int(b)-1,8)))%2::2])