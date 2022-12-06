while True:
    y = int(input())
    if y == 0:
        break
    if y in [1916, 1940, 1944]:
        state = 'Games cancelled'
    elif y % 4 == 0 and 1896 <= y <= 2020:
        state = 'Summer Olympics'
    elif y % 4 or y < 1896:
        state = 'No summer games'
    else:
        state = 'No city yet chosen'
    print(f'{y} {state}')