for _ in range(int(input())):
    input()
    word = ''
    MTF = 'abcdefghijklmnopqrstuvwxyz'
    for num in map(int, input().split()):
        word += MTF[num]
        MTF = MTF[num] + MTF[:num] + MTF[num+1:]
    print(word)