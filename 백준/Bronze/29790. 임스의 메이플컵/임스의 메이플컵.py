N, U, L = map(int, input().split())
if N >= 1000 and (U >= 8000 or L >= 260):
    print("Very Good")
elif N >= 1000:
    print("Good")
else:
    print("Bad")