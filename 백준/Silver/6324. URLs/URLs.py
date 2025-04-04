import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    s = input()
    i = s.find(':')
    protocol = s[:i]
    j = s.find(':', i + 3)
    k = s.find('/', i + 3)
    if j == -1 or k != -1 and k < j:
        port = "<default>"
        if k == -1:
            host = s[i + 3:]
            path = "<default>"
        else:
            host = s[i + 3:k]
            path = s[k + 1:]
    else:
        host = s[i + 3:j]
        k = s.find('/', j + 1)
        if k == -1:
            port = s[j + 1:]
            path = "<default>"
        else:
            port = s[j + 1:k]
            path = s[k + 1:]
    print(f"URL #{tc}")
    print(f"Protocol = {protocol}")
    print(f"Host     = {host}")
    print(f"Port     = {port}")
    print(f"Path     = {path}")
    print()