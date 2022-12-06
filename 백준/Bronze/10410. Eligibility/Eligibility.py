for _ in[0]*int(input()):
    s=input().split()
    x,y=map(lambda k:int(k.split('/')[0]),s[1:3])
    print(s[0],'eligible'if x>2009 or y>1990 else'coach petitions'if int(s[3])<41 else'ineligible')