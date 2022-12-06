for _ in range(int(input())):
    word = input()
    count = [-1]
    for s in word:
        if s == count[-1]:
            count[-2] += 1
        else:
            count += [1, s]
    print(''.join(map(str, count[1:])))