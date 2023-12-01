# [Silver IV] Bricks on the Wall - 14536 

[문제 링크](https://www.acmicpc.net/problem/14536) 

### 성능 요약

메모리: 110620 KB, 시간: 140 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2023년 12월 1일 14:18:29

### 문제 설명

<p>Ahmad has <em>n</em> bricks. He wants to build a wall using all bricks. He wants the wall’s dimensions to be as small as possible. The thickness of the <em>i</em>-th brick is <em>t<sub>i</sub></em> and its width is equal to <em>w<sub>i</sub></em>. In Ahmad’s case, the thickness of each brick is either 1 or 2. All bricks have the same heights.</p>

<p>Ahmad puts the bricks on the wall in the following way. First he select some of the bricks and put them vertically. Then he puts the rest of the bricks <strong>horizontally above</strong> the vertical bricks. The sum of widths of the horizontal bricks must be no more than the total thickness of the vertical bricks. A sample arrangement of the bricks is depicted in the ﬁgure.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14536/1.png" style="height:294px; width:291px"></p>

<p>Help Ahmad to ﬁnd the <strong>minimum total thickness</strong> of the vertical bricks that he can achieve.</p>

### 입력 

 <p>The ﬁrst line contains an integer <em>T</em>, (1 ≤ <em>T</em> ≤ 30) which is the number of test cases. For each case, the first line of input is an integer <em>n</em> (the number of bricks), (1 ≤ <em>n</em> ≤ 100). Each of the next <em>n</em> lines contains two integers <em>t<sub>i</sub></em> and <em>w<sub>i</sub></em> denoting the thickness and width of the <em>i</em>-th brick correspondingly, (1 ≤ <em>t<sub>i </sub></em>≤ 2, 1 ≤ <em>w<sub>i</sub></em> ≤ 100).</p>

### 출력 

 <p>For each test case, o the only line of the output print the minimum total thickness of the vertical bricks that we can achieve.</p>

