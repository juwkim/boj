input()
print(sum(int(i)*(i==i[::-1])for i in input().split()))