i = 1
while (t:=input()) != '0 0':
    print(f'Hole #{i}')
    i += 1
    p, s = map(int, t.split())
    if s == 1:
        print("Hole-in-one.")
    elif p - s > -2:
        print(["Par.", "Birdie.", "Eagle.", "Double eagle.", "Bogey."][p - s])
    else:
        print("Double Bogey.")
    print()