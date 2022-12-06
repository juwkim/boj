S, N = int(input()), int(input())
target = "I" + "OI" * S
text = input()
print(sum(target == text[i:i+2*S+1] for i in range(N-2*S)))