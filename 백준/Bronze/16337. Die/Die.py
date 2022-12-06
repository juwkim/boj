a = {'::::o::::': 1, 'o:::::::o': 2, '::o:::o::': 2,
     'o:::o:::o': 3, '::o:o:o::': 3, 'o:o:::o:o': 4,
     'o:o:o:o:o': 5, 'ooo:::ooo': 6, 'o:oo:oo:o': 6}
b = open(0).read().replace('\n','')
print(a[b] if b in a else 'unknown')