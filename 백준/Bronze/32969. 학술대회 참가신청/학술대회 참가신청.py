s = input()
if any(w in s for w in "social history language literacy".split()):
    print("digital humanities")
else:
    print("public bigdata")