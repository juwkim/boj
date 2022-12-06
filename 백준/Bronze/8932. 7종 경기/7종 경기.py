A = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
B = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
C = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]

T = int(input())
for _ in range(T):
    P = [*map(int, input().split())]
    score = sum([int(A[i] * abs(B[i] - P[i])**C[i]) for i in range(7)])
    print(score)