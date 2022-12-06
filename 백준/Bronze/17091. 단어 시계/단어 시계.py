a = {0: 'one', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
     19: 'nineteen', 20: 'twenty', 30: 'half'}
b = ['to', 'past']

h, m = map(int, [input(), input()])
s, t, u, v = min(m, 60-m), (h + (m > 30)) % 13, m < 31, 1 < m < 59
if m == 0:
    print(f"{a[h]} o' clock")
elif s == 15 or m == 30:
    print(f'{a[s]} {b[u]} {a[t]}')
elif s < 21:
    print(f'{a[s]} minute{["","s"][v]} {b[u]} {a[t]}')
else:
    print(f'twenty {a[s%10]} minutes {b[u]} {a[t]}')