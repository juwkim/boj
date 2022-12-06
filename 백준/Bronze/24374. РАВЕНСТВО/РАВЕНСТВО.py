l, c = input().split('=')
a, b = l.split('+')

for i in range(2, 37):
    try:
        if int(a, i) + int(b, i) == int(c, i):
            print(i)
            break
    except:
        continue