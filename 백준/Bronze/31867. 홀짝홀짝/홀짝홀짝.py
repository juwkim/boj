N = int(input())
t = 2 * sum(c in "02468" for c in input())
print((-1, 0, 1)[(t > N) - (t < N)])