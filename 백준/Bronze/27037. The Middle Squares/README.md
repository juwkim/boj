# [Bronze I] The Middle Squares - 27037 

[문제 링크](https://www.acmicpc.net/problem/27037) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Bessie's daghter, Cassie, returned from calf school with a new math problem. "I'm not sure I can do all the arithmetic," she whined.</p>

<p>"What is it you're doing?" asked her concerned mother.</p>

<p>"We are given a positive integer N less than 10,000," Cassie replied. "We treat it as four digit number, even if it's like 12 or something. We extract the second and third digits to create a new number which we then square to create another four digit number. We repeat that until we get to some number that we have already seen."</p>

<p>Help poor Cassie with her homework. Here is an example that starts with the number 4444:</p>

<pre>  N    2nd&3rd  Squared
4444 ... 0044 ... 1936
1936 ... 0093 ... 8649
8649 ... 0064 ... 4096
4096 ... 0009 ... 0081
0081 ... 0008 ... 0064
0064 ... 0006 ... 0036
0036 ... 0003 ... 0009
0009 ... 0000 ... 0000
0000 ... 0000 ... 0000</pre>

<p>This example required nine iterations to complete. The number 0000 results in a loop, since its resulting middle square is also 0000.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, N</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of iterations before some number is  duplicated.</li>
</ul>

