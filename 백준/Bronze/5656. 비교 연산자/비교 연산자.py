i = 1
while 'E' not in (s:=input()):
    print(f'Case {i}: {str(eval(s)).lower()}')
    i += 1