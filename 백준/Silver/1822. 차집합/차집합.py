g = lambda: map(int, input().split())

input()
s = {*g()} - {*g()}
print(len(s))
if len(s):
    print(*sorted(s))