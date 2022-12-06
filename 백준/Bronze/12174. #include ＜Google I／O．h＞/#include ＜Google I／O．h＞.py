for i in range(int(input())):
    B,s=int(input()),input().replace('O','0').replace('I','1')
    print(f"Case #{i+1}: {''.join([chr(int(s[i:i+8],2))for i in range(0,8*B,8)])}")