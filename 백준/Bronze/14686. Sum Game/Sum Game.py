g = lambda: [*map(int, input().split())]
n = int(input())
Swift, Semaphores = g(), g()
sum_swift, sum_semaphores = 0, 0
max_index = 0
for i in range(n):
    sum_swift += Swift[i]
    sum_semaphores += Semaphores[i]
    if sum_swift == sum_semaphores:
        max_index = i+1
print(max_index)