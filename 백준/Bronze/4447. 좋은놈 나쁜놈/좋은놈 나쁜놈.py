for _ in [0]*int(input()):
    s = input()
    g, b = 0, 0
    for i in s.lower():
        g += (i == 'g')
        b += (i == 'b')
    print(f"{s} is {['NEUTRAL', 'GOOD', 'A BADDY'][(g > b) - (g < b)]}")