# [Silver I] Flipping colors - 4280 

[문제 링크](https://www.acmicpc.net/problem/4280) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

수학

### 제출 일자

2025년 8월 7일 01:57:08

### 문제 설명

<p>A rectangle with sides parallel to the x-y axes and its left-lower corner at (0, 0) is being painted. The rectangle may be thought of as a flat-screen display with almost infinite resolution; initially the entire rectangle is black. Two numbers are given 0 < h, v < 1 and then</p>

<ul>
	<li>A vertical line is drawn dividing the horizontal sides of the rectangle in proportion h:1-h from the left.</li>
	<li>A horizontal line is drawn dividing the vertical sides of the rectangles in proportion v:1-v from the bottom up.</li>
	<li>These two lines divide the rectangle into four smaller rectangles.</li>
	<li>The upper left and the lower right sub-rectangles remain intact.</li>
	<li>The color of the other two rectangles is flipped (from black to white or from white to black) and now each of them is subject to the operation just performed on the bigger rectangle.</li>
	<li>This process continues (in principle) forever.</li>
</ul>

<p>Given a point in the original rectangle but not on the boundary of any rectangle that turns up in the process of painting, determine the color of the point.</p>

### 입력 

 <p>Input contains multiple cases. The first line of each case contains 4 numbers, the length of the rectangle H, the height of the rectangle V and then the numbers h and v. The next line contains one integer number n, the number of points to consider. The following n lines contain two numbers each, the x and the y coordinate of a point.</p>

### 출력 

 <p>Organize your output as shown in the sample. For each point from input print the color of the point.</p>

