s = input()
Min = '{'
for i in range(1, len(s)-1):
    a = s[i-1::-1]
    if a < Min:    
        for j in range(i+1, len(s)):
            b = s[j-1:i-1:-1]
            c = s[:j-1:-1]
            tmp = a + b + c
            if tmp < Min:
                Min = tmp
print(Min)