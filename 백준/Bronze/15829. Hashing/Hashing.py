input()
print(sum(31**i*(ord(s)-96)for i,s in enumerate(input()))%1234567891)