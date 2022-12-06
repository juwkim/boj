def preorder(root):
    global preord
    if root == '.':
        return
    preord += root
    preorder(dic[root][0])
    preorder(dic[root][1])

def inorder(root):
    global inord
    if root == '.':
        return
    inorder(dic[root][0])
    inord += root
    inorder(dic[root][1])

def postorder(root):
    global postord
    if root == '.':
        return
    postorder(dic[root][0])
    postorder(dic[root][1])
    postord += root
    
N = int(input())
dic = {}
root, l, r = input().split()
dic[root] = [l, r]
for _ in range(N-1):
    p, l, r = input().split()
    dic[p] = [l, r]

preord, inord, postord = "", "", ""
preorder(root)
inorder(root)
postorder(root)
print(preord, inord, postord, sep="\n")