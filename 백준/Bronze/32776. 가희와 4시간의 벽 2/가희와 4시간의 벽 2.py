Sab, Ma, Fab, Mb = map(int, open(0).read().split())
if Sab <= 240 or Sab <= Ma + Fab + Mb:
    print("high speed rail")
else:
    print("flight")