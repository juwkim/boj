D = {
    '0': ("xxxxx","x...x","x...x","x...x","x...x","x...x","xxxxx"),
    '1': ("....x","....x","....x","....x","....x","....x","....x"),
    '2': ("xxxxx","....x","....x","xxxxx","x....","x....","xxxxx"),
    '3': ("xxxxx","....x","....x","xxxxx","....x","....x","xxxxx"),
    '4': ("x...x","x...x","x...x","xxxxx","....x","....x","....x"),
    '5': ("xxxxx","x....","x....","xxxxx","....x","....x","xxxxx"),
    '6': ("xxxxx","x....","x....","xxxxx","x...x","x...x","xxxxx"),
    '7': ("xxxxx","....x","....x","....x","....x","....x","....x"),
    '8': ("xxxxx","x...x","x...x","xxxxx","x...x","x...x","xxxxx"),
    '9': ("xxxxx","x...x","x...x","xxxxx","....x","....x","xxxxx"),
    '+': (".....","..x..","..x..","xxxxx","..x..","..x..",".....")
}
R = {v: k for k, v in D.items()}
S = [input() for _ in range(7)]
W, i, T = len(S[0]), 0, []
while i + 5 <= W:
    blk = tuple(row[i:i+5] for row in S)
    T.append(R[blk])
    i += 6
a, b = map(int, ''.join(T).split('+'))
for r in range(7):
    print('.'.join(D[d][r] for d in str(a + b)))