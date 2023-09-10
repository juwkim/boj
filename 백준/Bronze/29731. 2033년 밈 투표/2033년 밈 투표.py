Set = {"Never gonna give you up",
       "Never gonna let you down",
       "Never gonna run around and desert you",
       "Never gonna make you cry",
       "Never gonna say goodbye",
       "Never gonna tell a lie and hurt you",
       "Never gonna stop"}
if all(input() in Set for _ in range(int(input()))):
    print("No")
else:
    print("Yes")