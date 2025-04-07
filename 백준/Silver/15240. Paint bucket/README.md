# [Silver I] Paint bucket - 15240 

[문제 링크](https://www.acmicpc.net/problem/15240) 

### 성능 요약

메모리: 140992 KB, 시간: 308 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 플러드 필, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 7일 17:21:24

### 문제 설명

<p dir="ltr"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15240/1.gif" style="float:right; height:144px; width:144px">One of the most time-saving operations when drawing on a computer (for example using Photoshop) is the “bucket fill”  operation.</p>

<p dir="ltr">When you select this tool and click on a (target) pixel of the image it will fill all the pixels that have the same color than the target pixel and are connected to it. Two pixels are connected if they share a side or if they are connected through a path of connected pixels.</p>

<p dir="ltr">Let’s see an example: In the following image, if we select the “fill” operation in an image editor program and click on the center of the image (orange pixel). The whole region will be painted orange. Notice that the pixels are not connected diagonally so two corners of the image remain white.</p>

<p dir="ltr" style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15240/2.png" style="height:150px; width:151px"> <img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15240/3.png" style="height:155px; width:153px"></p>

<p dir="ltr">Your task is: Given a matrix of digits representing the pixels, simulated what would be the result of a “fill” operation on given pixels. Thus, the colors will be represented with a number from 0 to 9.</p>

<p dir="ltr">Let’s see another example, now using digits instead of pixels. We have the following image:</p>

<pre>0000000
0111000
0111010
0000000
</pre>

<p dir="ltr">If we “fill” at position Y = 0, X = 0 with color 3, all the 0s get painted of color 3. Because all of them are recursively connected.</p>

<p dir="ltr">The result will be:</p>

<pre>3333333
3111333
3111313
3333333
</pre>

### 입력 

 <p dir="ltr">The first line will contain two integers R and C representing the number of rows and columns of the image.</p>

<p dir="ltr">The next R lines will contain C digits each representing the initial colors of the pixels.</p>

<p dir="ltr">The last line will contain 3 integers Y, X and K representing the row and column where we want to apply the “fill” operation and the color to use.</p>

<p dir="ltr">The images will be smaller than 1000 x 1000 pixels.</p>

<p dir="ltr">The colors are limited to a single digit from 0 to 9.</p>

### 출력 

 <p dir="ltr">Print the resulting image after applying the operation in the same format as the input.</p>

