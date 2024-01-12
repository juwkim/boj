import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드들을 저장하는 딕셔너리
        self.is_end_of_word = False  # 해당 노드에서 끝나는 단어인지 여부

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.is_end_of_word:
                return False
        node.is_end_of_word = True
        return True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

for _ in range(int(input())):
    trie = Trie()
    words = [input() for _ in range(int(input()))]
    ans = "YES"
    for word in words:
        if trie.starts_with_prefix(word):
            ans = "NO"
            break
        if not trie.insert(word):
            ans = "NO"
            break
    print(ans)