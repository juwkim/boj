# [Silver IV] Anniversary Cake - 13473 

[문제 링크](https://www.acmicpc.net/problem/13473) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구성적(constructive), 기하학(geometry), 수학(math)

### 문제 설명

<p>Two students, Adam and Anton, are celebrating two-year anniversary of not passing their Math Logic exam. After very careful search in a local supermarket, they bought a rectangular cake with integer dimensions and two candles.</p>

<p>Later in the campus Adam put the candles into different integer points of the cake and gave a knife to Anton to cut the cake. The cut should start and end at integer points at the edges of the cake, and it should not touch the candles. Also each piece should have exactly one candle at it. Please, help Anton to find the starting and ending points of the cut.</p>

<p><img alt="" src="" style="height:147px; width:330px"></p>

<p>A 7 × 3 cake and two candles at (2, 2) and (3, 2).<br>
Anton can cut this cake through (0, 0) and (4, 3).</p>

### 입력 

 <p>The single line of the input contains six integers: w, h — cake dimensions; a<sub>x</sub>, a<sub>y</sub> — x and y coordinates of the first candle; b<sub>x</sub>, b<sub>y</sub> — the coordinates of the second candle (3 ≤ w, h ≤ 10<sup>9</sup>; 0 < a<sub>x</sub>, b<sub>x</sub> < w; 0 < a<sub>y</sub>, b<sub>y</sub> < h; a<sub>x</sub> ≠ b<sub>x</sub> or a<sub>y </sub>≠ b<sub>y</sub>).</p>

### 출력 

 <p>Output four integers s<sub>x</sub>, s<sub>y</sub>, e<sub>x</sub>, and e<sub>y</sub> — the starting and ending coordinates of the cut. Both starting and ending point of the cut should belong to the sides of the cake.</p>

<p>If there are several solutions, output any of them.</p>

