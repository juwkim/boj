def solve(s):

    if len(s) < 9 or len(s) > 20:
        return False    

    if sum(c.islower() for c in s) < 2:
        return False

    if sum(c.isupper() for c in s) < 2:
        return False
    
    if all(c.isdigit() == False for c in s):
        return False
    
    if sum(c.isalnum() == False for c in s) < 2:
        return False
    
    if any(s[i] == s[i + 1] == s[i + 2] for i in range(len(s) - 2)):
        return False
    
    alnum = [c.lower() for c in s if c.isalnum()]
    alnum_r = alnum[::-1]
    if alnum == alnum_r:
        return False
    
    words = ['password', 'virginia', 'cavalier', 'code']
    for word in words:
        
        idx = 0
        for c in alnum:
            if c == word[idx]:
                idx += 1
                if idx == len(word):
                    break
        if idx == len(word):
            return False

        idx = 0
        for c in alnum_r:
            if c == word[idx]:
                idx += 1
                if idx == len(word):
                    break
        if idx == len(word):
            return False    
    
    return True
    
ans = ['Invalid Password', 'Valid Password']
for _ in range(int(input())):
    s = input()   
    print(ans[solve(s)])