dic = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
for _ in range(int(input())):
    m, d, y = input().split()
    d, y = int(d[:-1]), int(y)
    if d < 1 or d > 31 or m not in dic:
        print('Invalid')
    else:
        print("%02d/%02d/%02d" % (dic[m], d, y % 100))