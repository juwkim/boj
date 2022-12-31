import sys
sys.setrecursionlimit(10 ** 5)
def g(): return [*map(int, input().split())]


def findPreorder(inStart, inEnd, postStart, postEnd):

    if inStart > inEnd or postStart > postEnd:
        return

    rootIndex = Index[postorder[postEnd]]
    leftSize = rootIndex - inStart

    print(inorder[rootIndex], end=' ')
    findPreorder(inStart, rootIndex - 1, postStart, postStart + leftSize - 1)
    findPreorder(rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1)


n = int(input())
inorder = g()
postorder = g()

Index = [0] * (n + 1)
for idx, node in enumerate(inorder):
    Index[node] = idx

findPreorder(0, n - 1, 0, n - 1)