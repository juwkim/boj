MBTI = 'EISNTFJP'
for i in input():
    k = MBTI.index(i)
    print(MBTI[1-k+k//2*4], end='')