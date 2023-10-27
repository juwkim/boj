import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    try:
        input()
        node, edge = bytearray(26), [bytearray(26) for _ in range(26)]
        while (s:=input()) != "GRAPH END":
            l = s.split()
            for c in l:
                node[ord(c[0]) - 97] = 1
            s = ord(l[0]) - 97
            for e in map(lambda x: ord(x) - 97, l[1:]):
                p, q = sorted([s, e])
                edge[p][q] = 1
        nodes = sum(node)
        edges = sum(edge[i][j] for i in range(26) for j in range(i + 1, 26))
        print(f"NODES {sum(node)} EDGES {edges}")
    except:
        break