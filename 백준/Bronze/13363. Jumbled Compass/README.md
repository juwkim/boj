# [Bronze III] Jumbled Compass - 13363 

[문제 링크](https://www.acmicpc.net/problem/13363) 

### 성능 요약

메모리: 121220 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 많은 조건 분기(case_work), 구현(implementation), 수학(math)

### 문제 설명

<p>Jonas is developing the JUxtaPhone and is tasked with animating the compass needle. The API is simple: the compass needle is currently in some direction (between 0 and 359 degrees, with north being 0, east being 90), and is being animated by giving the degrees to spin it. If the needle is pointing north, and you give the compass an input of 90, it will spin clockwise (positive numbers mean clockwise direction) to stop at east, whereas an input of −45 would spin it counterclockwise to stop at north west.</p>

<p>The compass gives the current direction the phone is pointing and Jonas’ task is to animate the needle taking the shortest path from the current needle direction to the correct direction. Many ifs, moduli, and even an arctan later, he is still not convinced his minimumDistance function is correct; he calls you on the phone.</p>

### 입력 

 <p>The first line of input contains an integer n<sub>1</sub> (0 ≤ n<sub>1</sub> ≤ 359), the current direction of the needle. The second line of input contains an integer n<sub>2</sub> (0 ≤ n<sub>2</sub> ≤ 359), the correct direction of the needle.</p>

### 출력 

 <p>Output the change in direction that would make the needle spin the shortest distance from n<sub>1</sub> to n<sub>2</sub>. A positive change indicates spinning the needle clockwise, and a negative change indicates spinning the needle counter-clockwise. If the two input numbers are diametrically opposed, the needle should travel clockwise. I.e., in this case, output 180 rather than −180.</p>

