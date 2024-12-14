# [Silver II] Secret of Chocolate Poles - 15329 

[문제 링크](https://www.acmicpc.net/problem/15329) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 12월 15일 00:20:19

### 문제 설명

<p>Wendy, the master of a chocolate shop, is thinking of displaying poles of chocolate disks in the showcase. She can use three kinds of chocolate disks: white thin disks, dark thin disks, and dark thick disks. The thin disks are 1 cm thick, and the thick disks are k cm thick. Disks will be piled in glass cylinders.</p>

<p>Each pole should satisfy the following conditions for her secret mission, which we cannot tell.</p>

<ul>
	<li>A pole should consist of at least one disk.</li>
	<li>The total thickness of disks in a pole should be less than or equal to l cm.</li>
	<li>The top disk and the bottom disk of a pole should be dark.</li>
	<li>A disk directly upon a white disk should be dark and vice versa.</li>
</ul>

<p>As examples, six side views of poles are drawn in Figure A.1. These are the only possible side views she can make when l = 5 and k = 3.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15329/1.png" style="height:159px; width:273px"></p>

<p style="text-align:center">Figure A.1. Six chocolate poles corresponding to Sample Input 1</p>

<p>Your task is to count the number of distinct side views she can make for given l and k to help her accomplish her secret mission.</p>

### 입력 

 <p>The input consists of a single test case in the following format.</p>

<pre>l k</pre>

<p>Here, the maximum possible total thickness of disks in a pole is l cm, and the thickness of the thick disks is k cm. l and k are integers satisfying 1 ≤ l ≤ 100 and 2 ≤ k ≤ 10.</p>

### 출력 

 <p>Output the number of possible distinct patterns.</p>

