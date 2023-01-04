def g(): return [*map(int, input().split())]

for _ in range(int(input())):
    input()
    N = int(input())
    if len(set(g())) == len(set(g())):
        print("what a lovely party")
    else:
        print("you've messed up, Cornell")