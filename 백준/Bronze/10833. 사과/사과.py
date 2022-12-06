N = int(input())
remainder = 0
for _ in range(N):
    students, apples = map(int, input().split())
    remainder += apples % students
print(remainder)