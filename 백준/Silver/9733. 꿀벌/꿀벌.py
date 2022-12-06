from statistics import Counter
a = Counter()
while True:
    try:
        a += Counter(input().split())
    except:
        break

cnt = sum(a.values())
for i in ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']:
    print(f'{i} {a[i]} {a[i] / cnt:.2f}')
print(f'Total {cnt} 1.00')