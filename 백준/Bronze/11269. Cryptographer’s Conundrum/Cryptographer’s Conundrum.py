s = input()
print(sum(s[i] != 'PER'[i%3] for i in range(len(s))))