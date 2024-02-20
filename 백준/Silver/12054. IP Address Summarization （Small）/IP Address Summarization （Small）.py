import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num, l):
        node = self.root
        parent = []
        for i in range(l):
            bit = (num >> (31 - i)) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            parent.append(node)
            node = node.children[bit]
            if node.is_end:
                return
        node.is_end = True
        for p in reversed(parent):
            if p.children[0] and p.children[1]:
                if p.children[0].is_end and p.children[1].is_end:
                    p.is_end = True
                else:
                    break

    def dfs(self, node, depth, num, res):
        if node.is_end:
            res.append((num, depth))
            return
        if node.children[0]:
            self.dfs(node.children[0], depth + 1, (num << 1) | 0, res)
        if node.children[1]:
            self.dfs(node.children[1], depth + 1, (num << 1) | 1, res)

for tc in range(1, 1 + int(input())):
    buf = []
    for _ in range(int(input())):
        s, l = input().split('/')
        a, b, c, d = map(int, s.split('.'))
        num = (a << 24) + (b << 16) + (c << 8) + d
        buf.append((num, int(l)))
    buf.sort()
    trie = Trie()
    for num, l in buf:
        trie.insert(num, l)
    print(f'Case #{tc}:')
    res = []
    trie.dfs(trie.root, 0, 0, res)
    for num, l in res:
        num <<= 32 - l
        print(f'{num >> 24 & 255}.{num >> 16 & 255}.{num >> 8 & 255}.{num & 255}/{l}')
