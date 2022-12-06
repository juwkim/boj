n = int(input())
a, b = map(int, [input(), input()])
if n%2 and str(a+b).count('0') == 0:
    print('Deletion succeeded')
elif n%2 == 0 and a == b:
    print('Deletion succeeded')
else:
    print('Deletion failed')