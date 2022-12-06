while True:
    try:
        cards = [input() for _ in range(12)]
        buf = []
        for i in range(10):
            for j in range(i+1, 11):
                for k in range(j+1, 12):
                    a, b, c = cards[i], cards[j], cards[k]
                    if all(x == y == z or (x != y and y != z and z != x) for x, y, z in zip(a, b, c)):
                        buf.append((a, b, c))

        print('CARDS: ', *cards)
        if buf:
            print('SETS:   1. ', *buf[0])
            for i in range(1, len(buf)):
                print(f'        {i+1}. ', *buf[i])
        else:
            print('SETS:   *** None Found ***')
        print(input())
    except:
        break