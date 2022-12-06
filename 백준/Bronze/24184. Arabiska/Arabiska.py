n = int(input())
words = input().split()
temp = []
for word in words:
    a = [i in 'aeiouy' for i in word] + [1, 1]
    b = [word[i] for i in range(len(word)) if a[i] == 0 or a[i+1] + a[i+2]]
    temp.append(''.join(b))
print(' '.join(temp)[::-1])