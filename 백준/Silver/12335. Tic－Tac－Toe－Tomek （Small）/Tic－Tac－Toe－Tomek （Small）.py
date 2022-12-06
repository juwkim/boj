X_win = set(['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX'])
O_win = set(['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO'])
for _ in range(1, 1 + int(input())):
    Map = [input() for _ in range(4)]
    Map += [''.join(l) for l in zip(*Map)]
    Map.append(''.join([Map[i][i] for i in range(4)]))
    Map.append(''.join([Map[3-i][i] for i in range(4)]))
    
    if any(line in X_win for line in Map):
        ans = 'X won'
    elif any(line in O_win for line in Map):
        ans = 'O won'
    elif any('.' in line for line in Map):
        ans = 'Game has not completed'
    else:
        ans = 'Draw'
    
    print(f'Case #{_}:', ans)
    input()