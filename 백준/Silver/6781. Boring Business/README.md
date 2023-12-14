# [Silver IV] Boring Business - 6781 

[문제 링크](https://www.acmicpc.net/problem/6781) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2023년 12월 15일 07:01:40

### 문제 설명

<p>Boring is a type of drilling, specifically, the drilling of a tunnel, well, or hole in the earth. With some recent events, such as the Deepwater Horizon oil spill and the rescue of Chilean miners, the public became aware of the sophistication of the current boring technology. Using the technique known as geosteering, drill operators can drill wells vertically, horizontally, or even on a slant angle.</p>

<p>A well plan is prepared before drilling, which specifies a sequence of lines, representing a geometrical shape of the future well. However, as new information becomes available during drilling, the model can be updated and the well plan modified.</p>

<p>Your task is to write a program that verifies validity of a well plan by verifying that the borehole will not intersect itself. A two-dimensional well plan is used to represent a vertical cross-section of the borehole, and this well plan includes some drilling that has occurred starting at (0, −1) and moving to (−1, −5). You will encode in your program the current well plan shown in the figure below:</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/6781/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-03-24%20%EC%98%A4%ED%9B%84%201.36.30.png" style="height:235px; width:396px"></p>

### 입력 

 <p>The input consists of a sequence of drilling command pairs. A drilling command pair begins with one of four direction indicators (<code>d</code> for down, <code>u</code> for up, <code>l</code> for left, and <code>r</code> for right) followed by a positive length. There is an additional drilling command indicated by <code>q</code> (quit) followed by any integer, which indicates the program should stop execution. You can assume that the input is such that the drill point will not:</p>

<ul>
	<li>rise above the ground, nor</li>
	<li>be more than 200 units below ground, nor</li>
	<li>be more than 200 units to the left of the original starting point, nor</li>
	<li>be more than 200 units to the right of the original starting point</li>
</ul>

### 출력 

 <p>The program should continue to monitor drilling assuming that the well shown in the figure has already been made. As we can see (−1, −5) is the starting position for your program. After each command, the program must output one line with the coordinates of the new position of the drill, and one of the two comments <code>safe</code>, if there has been no intersection with a previous position or <code>DANGER</code> if there has been an intersection with a previous borehole location. After detecting and reporting a self-intersection, your program must stop.</p>

