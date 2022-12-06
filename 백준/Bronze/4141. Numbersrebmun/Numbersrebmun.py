for _ in[0]*int(input()):
    n=[(ord(s)-59)//3-(s in'SVYZ')for s in input().upper()]
    print('YNEOS'[n!=n[::-1]::2])