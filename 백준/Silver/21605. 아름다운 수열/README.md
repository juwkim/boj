# [Silver I] 아름다운 수열 - 21605 

[문제 링크](https://www.acmicpc.net/problem/21605) 

### 성능 요약

메모리: 114584 KB, 시간: 112 ms

### 분류

구성적(constructive)

### 문제 설명

<p>길이 $2N$인 수열 $A$의 아름다움 $b(A)$를 아래와 같이 정의합니다.</p>

<p style="text-align: center;">$B_i = \left\{ \begin{array}{lr} 0, & \text {for } i=0 \\ B_{i-1} \times A_{2i-1} + A_{2i} & \text {for } 1 \le i \le N \end{array} \right\}$</p>

<p style="text-align: center;">$b(A) = B_N$</p>

<p>아래 조건을 만족하는 수열 중 아름다움이 최대인 것을 출력합시다.</p>

<ul>
	<li>수열의 길이는 $2N$입니다.</li>
	<li>수열의 원소 중 $N$개는 1, $N$개는 -1입니다.</li>
</ul>

### 입력 

 <p>첫 줄에 $N$이 주어집니다.</p>

### 출력 

 <p>각 항을 띄어쓰기로 구분하여 아름다움이 최대인 수열을 출력합니다.</p>

