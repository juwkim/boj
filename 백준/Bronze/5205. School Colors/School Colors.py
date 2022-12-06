def Dist(A, B):
    return (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2


k = int(input())
for i in range(1, k + 1):
    max_dist, check = 0, []
    
    n = int(input())
    nums = [[*map(int, input().split())] for _ in range(n)]
    
    for j in range(n-1):
        for k in range(j+1, n):
            dist = Dist(nums[j], nums[k])

            if dist > max_dist:
                check = [j+1, k+1]
                max_dist = dist
            elif dist == max_dist:
                check += [j+1, k+1]
    
    print(f"Data Set {i}:")
    for s in range(len(check)//2):
        print(check[2*s], check[2*s+1])