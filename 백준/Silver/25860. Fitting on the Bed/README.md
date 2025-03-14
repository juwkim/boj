# [Silver II] Fitting on the Bed - 25860 

[문제 링크](https://www.acmicpc.net/problem/25860) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

기하학, 수학

### 제출 일자

2025년 3월 14일 23:01:30

### 문제 설명

<p>Arup’s daughter, Anya, doesn’t like sleeping in a bed in the usual way. In particular, she is willing to put her head anywhere, and furthermore, she’s willing to lie in any direction. For the purposes of this problem, Anya, who is quite skinny, as she’s only at the fifth percentile in weight, will be modeled as a line segment with her head being one of the end points of the segment. The bed will be modeled as a rectangle with the bottom left corner with coordinates (0, 0), the top left corner with coordinates (0, L), where L is the length of the bed, and the top right corner with coordinates (W, L), where W is the width of the bed. In the left diagram below, Anya’s head is near the top left corner and she’s sleeping completely sideways, off the bed - this corresponds to the first sample case. In the right diagram below, her head starts at a point a bit below where it starts in the first diagram, but she’s sleeping at a diagonal, which allows her to fit on the bed!</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/611919b1-984a-49bf-bc52-66c4964323f2/-/preview/" style="width: 441px; height: 245px;"></p>

<p>Given the size of the bed, the location of Anya’s head, her height, and the angle in which her body is in relation to her head (here we use 0 degrees to indicate that her body is going straight to the right of her head and 90 degrees to indicate that her body is going above her head), determine if Anya is fully fitting within the bed or not. (Note: a normal sleeping position would be having your head near (W/2, L) with your body in the direction of 270 degrees.)</p>

### 입력 

 <p>The first line of input contains three positive integers: L (L ≤ 500), the length of the bed in centimeters, W (W ≤ 500), the width of the bed in centimeters, and H (H ≤ 200), Anya’s height in centimeters. The second line of input contains three non-negative integers: x (x ≤ W), the number of centimeters from the left side of the bed Anya’s head is, y (y ≤ L), the number of centimeters from the bottom of the bed Anya’s head is, and a (a ≤ 359), the angle in degrees Anya’s body is facing in relation to her head.</p>

### 출력 

 <p>On a line by itself, output “YES” (no quotes) if Anya completely fits on the bed, or “NO”, otherwise. Note: for all cases where Anya doesn’t fit on the bed, at least 1% of her body will be off the bed. She’s considered on the bed if part or all of her touches edges of the bed but none of her body extends off the bed.</p>

