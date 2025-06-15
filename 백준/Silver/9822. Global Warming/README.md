# [Silver I] Global Warming - 9822 

[문제 링크](https://www.acmicpc.net/problem/9822) 

### 성능 요약

메모리: 227496 KB, 시간: 1764 ms

### 분류

구현, 시뮬레이션, 정렬

### 제출 일자

2025년 6월 15일 21:57:53

### 문제 설명

<p>A scientist wants to study how the rising sea level changes the landscape, in particular, how it changes the number of islands. He first investigates one-dimensional worlds. An onedimensional world is represented by a sequence of non-negative integers <h<sub>0</sub>, h<sub>1</sub>, . . . , h<sub>n−1</sub>>, where each integer h<sub>i</sub> is the altitude at the location i. The following figure depicts an example of such world represented by the sequence <5, 6, 1, 3, 2, 9, 8>.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/46e64fd7-3fd0-418e-9896-313617de5a4f/-/preview/" style="width: 345px; height: 293px;"></p>

<p>Now, if the sea level is at altitude 2.5, there are 3 islands formed by landmass of the first two columns, the fourth column and the last two columns. Furthermore, if the sea level is at altitude 3.5, there are only 2 islands. When the sea level is at altitude x, landmass with altitude x is considered to be submerged under the sea. Hence, if the sea level is at altitude 3, there are 2 islands. Note that having 3 islands is the maximum among all possible sea levels.</p>

<p>Given a one-dimensional world, the scientist wants to find the maximum number of islands among all sea levels.</p>

### 입력 

 <p>Your program must read from the standard input. The first line in the input contains the integer n, the total number of integers in the sequence. Next, it is followed by n lines where each line contains an integer. These n lines represent the sequence <h<sub>0</sub>, h<sub>1</sub>, . . . , h<sub>n−1</sub>>. All numbers in the sequence are non-negative and smaller than 2<sup>30</sup>.</p>

### 출력 

 <p>Your program must write to the standard output an integer, which is the maximum number of islands.</p>

