N = int(input())
print("soccer " * N, flush=True)
for course in input().split():
    if course == "swimming":
        print("bowling", end=' ')
    else:
        print("swimming", end=' ')