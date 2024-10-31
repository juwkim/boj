g = lambda: map(int, input().split())
(xs, ys), (xt, yt), (xp, yp) = g(), g(), g()
P = (-10001, 10001)[xs < xp]
if (xs - xp) * (xt - xp) < 0:
    print(f"{4}\n{-P} {ys}\n{-P} {P}\n{P} {P}\n{P} {yt}")
else:
    print(f"{2}\n{-P} {ys}\n{-P} {yt}")