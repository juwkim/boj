i = 1
while 'END' != (s:= input()):
    print(f'Case {i}: {["different", "same"][sorted(s) == sorted(input())]}')
    i += 1