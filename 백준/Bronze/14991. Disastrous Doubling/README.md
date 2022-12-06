# [Bronze II] Disastrous Doubling - 14991 

[문제 링크](https://www.acmicpc.net/problem/14991) 

### 성능 요약

메모리: 42132 KB, 시간: 452 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>A scientist, E. Collie, is going to do some experiments with bacteria. Right now, she has one bacterium. She already knows that this species of bacteria doubles itself every hour. Hence, after one hour there will be 2 bacteria. E.</p>

<p>E. Collie will do one experiment every hour, for n consecutive hours. She starts the first experiment exactly one hour after the first bacterium starts growing. In experiment i she will need b<sub>i</sub> bacteria.</p>

<p>How many bacteria will be left directly after starting the last experiment? If at any point there are not enough bacteria to do the experiment, print “error”.</p>

<p>Since the answer may be very large, please print it modulo 10<sup>9</sup> + 7.</p>

### 입력 

 <p>The input consists of two lines.</p>

<ul>
	<li>The first line contains an integer 1 ≤ n ≤ 10<sup>5</sup>, the number of experiments.</li>
	<li>The second line contains n integers b<sub>1</sub>, . . . , b<sub>n</sub>, where 0 ≤ b<sub>i</sub> ≤ 2<sup>60</sup> is the number of bacteria used in the ith experiment.</li>
</ul>

### 출력 

 <p>Output a single line containing the number of bacteria that remains after doing all the experiments, or “error”.</p>

