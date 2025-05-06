class Post:
    def __init__(self, M=None):
        self.M = M
        self.children = []

def solve(node, depth):
    print("." * depth + node.M)
    for child in node.children:
        solve(child, depth + 1)

posts = [Post()]
parents = [0]
for _ in range(int(input())):
    k = int(input())
    parents.append(k)
    M = Post(input())
    posts.append(M)
    posts[k].children.append(M)
solve(posts[1], 0)