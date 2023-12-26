n=int(input())
print(("Second","First")[(int(input().split()[-1])-n)&1])