import sys
sys.setrecursionlimit(10 ** 5)

def findPostorder(rootIndex, end):

    if rootIndex > end:
        return
    
    idx = rootIndex + 1
    while idx < len(preorder) and preorder[idx] < preorder[rootIndex]:
        idx += 1
    
    findPostorder(rootIndex + 1, idx - 1)
    findPostorder(idx, end)
    print(preorder[rootIndex])

preorder = [*map(int, open(0))]
findPostorder(0, len(preorder) - 1)