for _ in range(int(input())):
    score = [[*map(int, input().split())] for _ in range(9)]
    yonsei = sum(i[0] for i in score)
    korea = sum(i[1] for i in score)
    print('Yonsei' if yonsei > korea else 'Korea' if yonsei < korea else 'Draw')