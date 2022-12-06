while (s:=input()) != '#':
    card = s.split()[:-1]
    odd = sum(s == 'A' or int(s)%2 for s in card)
    even = len(card) - odd
    print(['Draw', 'Cheryl', 'Tania'][(odd > even) - (odd < even)])