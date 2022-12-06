while n:= int(input()):
    top, north, west = 1, 2, 3
    for _ in range(n):
        cmd = input()
        if cmd == 'north':
            top, north = 7 - north, top
        elif cmd == 'south':
            top, north = north, 7 - top
        elif cmd == 'east':
            top, west = west, 7 - top
        else:
            top, west = 7 - west, top
    print(top)