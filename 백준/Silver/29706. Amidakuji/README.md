# [Silver IV] Amidakuji - 29706 

[문제 링크](https://www.acmicpc.net/problem/29706) 

### 성능 요약

메모리: 111520 KB, 시간: 220 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2024년 4월 29일 23:43:33

### 문제 설명

<p>Amidakuji is a method of lottery popular in East Asia. It is often used when a number of gifts are distributed to people or when a number of tasks are assigned.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7e181bc7-f1ed-45fd-b5f9-2d26e1a058f2/-/preview/" style="width: 325px; height: 350px;"></p>

<p style="text-align: center;">Figure B-1: An example of amidakuji</p>

<p>Figure B-1 shows an example of amidakuji, which corresponds to the first dataset of Sample Input. A number of vertical lines are drawn. The number of lines is the same as the number of participants. Some number of horizontal bars are drawn between some pairs of adjacent vertical lines. The number and positions of these bars are arbitrary, but no two bars should share their ends. Usually, many horizontal bars are drawn at random.</p>

<p>To use an amidakuji, first, the names of an item, a gift or a task, are written down at the bottom end of vertical lines. Then, each participant chooses the top end of a vertical line, different from one another. Participants trace down the chosen line from the top. When reaching a T-junction with a horizontal bar, that bar is followed, switching to the adjacent vertical line it is connected, and the trace continues downward. When the bottom end of a vertical line is reached, the item written there is the awarded gift or the assigned task. Figure B-2 shows the case when the top end P is chosen. In this case, the item at R is obtained.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4e15d2e0-38af-4ba0-ab44-079ebb510303/-/preview/" style="width: 325px; height: 363px;"></p>

<p style="text-align: center;">Figure B-2: The trace from P</p>

<p>Assume that the participant choosing P of Figure B-2 wants the item at Q, which is not fulfilled. But wait, a special rule just introduced may grant that wish. The new rule allows adding a single horizontal bar at an arbitrary position. Actually, adding a bar marked X in Figure B-3 will make the trace reach Q.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/43474c55-c65f-4c6c-a488-7a22c1d45997/-/preview/" style="width: 325px; height: 363px;"></p>

<p style="text-align: center;">Figure B-3: The new trace after adding a horizontal bar</p>

<p>Your task in this problem is to write a program that finds the position of a horizontal bar to add to the given amidakuji for making the trace starting from the top end of the specified vertical line reach the bottom end of the specified vertical line.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<blockquote>
<p><i>n</i> <i>m</i> <i>p</i> <i>q</i></p>

<p><i>x</i><sub>1</sub> ⋯ <i>x<sub>m</sub></i></p>
</blockquote>

<p>All the input items in a dataset are positive integers. <i>n</i> is the number of vertical lines. <i>m</i> is the number of horizontal bars in the original amidakuji. The participant choosing the top end of the <i>p</i>-th line from the left wants the trace to reach the bottom end of the <i>q</i>-th line from the left. You can assume 2 ≤ <i>n</i> ≤ 50, <i>m</i> ≤ 500, <i>p</i> ≤ <i>n</i>, and <i>q</i> ≤ <i>n</i> hold.</p>

<p><i>x</i><sub>1</sub>, …, and <i>x<sub>m</sub></i> give the positions of horizontal bars in the original amidakuji. <i>x<sub>k</sub></i> is the position of the <i>k</i>-th bar from the top. Thus, vertical positions of all bars are different. <i>x<sub>k</sub></i> ≤ <i>n</i> − 1 holds. The bar connects the <i>x<sub>k</sub></i>-th line from the left and the (<i>x<sub>k</sub></i> + 1)-th line.</p>

<p>The end of the input is indicated by a line consisting of four zeros. The number of datasets in the input does not exceed 300.</p>

### 출력 

 <p>For each dataset, output a single line, which is one of the following.</p>

<ul>
	<li>If <i>q</i> can be reached from <i>p</i> without adding a bar, <code>OK</code>.</li>
	<li>If not, and adding a single bar cannot make <i>q</i> reachable from <i>p</i>, <code>NG</code>.</li>
	<li>Otherwise, two integers <i>x</i> and <i>y</i> separated by a space, which represent the position of the bar to be added. A bar connecting the <i>x</i>-th line from the left and the (<i>x</i> + 1)-th line should be added at the height between the <i>y</i>-th bar from the top and the (<i>y</i> + 1)-th bar. If the bar is to be added at a position higher than the uppermost bar, <i>y</i> should be 0. If the bar is to be added at a position lower than the lowermost bar, <i>y</i> should be equal to <i>m</i>. If there are two or more appropriate positions to add a bar, the position with the minimum <i>y</i> should be chosen.</li>
</ul>

<p><code>OK</code> and <code>NG</code> should be in uppercase.</p>

