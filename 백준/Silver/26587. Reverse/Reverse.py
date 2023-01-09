while True:
    try:
        words = input().split()
        l, r = 0, len(words) - 1
        while l < r:
            while l < r and all(words[l].startswith(i) == False for i in 'aeiouAEIOU'):
                l += 1
            
            while l < r and all(words[r].startswith(i) == False for i in 'aeiouAEIOU'):
                r -= 1
            
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        print(*words)
    except:
        break