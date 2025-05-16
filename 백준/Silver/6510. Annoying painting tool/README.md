# [Silver I] Annoying painting tool - 6510 

[문제 링크](https://www.acmicpc.net/problem/6510) 

### 성능 요약

메모리: 112648 KB, 시간: 352 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 5월 17일 05:31:59

### 문제 설명

<p>Maybe you wonder what an annoying painting tool is? First of all, the painting tool we speak of supports only black and white. Therefore, a picture consists of a rectangular area of pixels, which are either black or white. Second, there is only one operation how to change the colour of pixels:</p>

<p>Select a rectangular area of r rows and c columns of pixels, which is completely inside the picture. As a result of the operation, each pixel inside the selected rectangle changes its colour (from black to white, or from white to black).</p>

<p>Initially, all pixels are white. To create a picture, the operation described above can be applied several times. Can you paint a certain picture which you have in mind?</p>

### 입력 

 <p>The input contains several test cases. Each test case starts with one line containing four integers n, m, r and c. (<em>1 ≤ r ≤ n ≤ 100, 1 ≤ c ≤ m ≤ 100</em>), The following n lines each describe one row of pixels of the painting you want to create. The i<sup>th</sup> line consists of m characters describing the desired pixel values of the i<sup>th</sup> row in the finished painting ('0' indicates white, '1' indicates black).</p>

<p>The last test case is followed by a line containing four zeros.</p>

### 출력 

 <p>For each test case, print the minimum number of operations needed to create the painting, or -1 if it is impossible.</p>

