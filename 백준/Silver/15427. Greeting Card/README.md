# [Silver II] Greeting Card - 15427 

[문제 링크](https://www.acmicpc.net/problem/15427) 

### 성능 요약

메모리: 127300 KB, 시간: 296 ms

### 분류

자료 구조, 기하학, 해시를 사용한 집합과 맵, 수학, 런타임 전의 전처리, 피타고라스 정리

### 제출 일자

2024년 12월 18일 00:11:39

### 문제 설명

<p>Quido plans to send a New Year greeting to his friend Hugo. He has recently acquired access to an advanced high-precision plotter and he is planning to print the greeting card on the plotter.</p>

<p>Here’s how the plotter operates. In step one, the plotter plots an intricate pattern of n dots on the paper. In step two, the picture in the greeting emerges when the plotter connects by a straight segment each pair of dots that are exactly 2 018 length units apart.</p>

<p>The plotter uses a special holographic ink, which has a limited supply. Quido wants to know the number of all plotted segments in the picture to be sure that there is enough ink to complete the job.</p>

### 입력 

 <p>The first line of input contains a positive integer n specifying the number of plotted points. The following n lines each contain a pair of space-separated integer coordinates indicating one plotted point. Each coordinate is non-negative and less than 2<sup>31</sup>. There are at most 10<sup>5</sup> points, all of them are distinct.</p>

<p>In this problem, all coordinates and distances are expressed in plotter length units, the length of the unit in the x-direction and in the y-direction is the same.</p>

### 출력 

 <p>The output contains a single integer equal to the number of pairs of points which are exactly 2 018 length units apart.</p>

