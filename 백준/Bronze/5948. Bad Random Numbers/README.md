# [Bronze I] Bad Random Numbers - 5948 

[문제 링크](https://www.acmicpc.net/problem/5948) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>Bessie is trying to generate random numbers. She stumbled upon an old reference to the 'middle square' method for making numbers that appear to be random. It works like this:</p>

<ul>
	<li>Pick a starting four digit number (1 <= N <= 9999)</li>
	<li>Extract its middle two digits (the hundreds and tens digit) as a number</li>
	<li>Compute the square of those two digits</li>
	<li>That square is the 'random number' and becomes the new starting number</li>
</ul>

<p>Here's a sample:</p>

<pre>                Num  Middle  Square
               7339    33     1089
               1089     8       64
                 64     6       36
                 36     3        9
                  9     0        0
                  0     0        0</pre>

<p>The 'pigeon hole principle' tells us that the random numbers surely must repeat after no more than 10,000 of them -- and the sequence above repeats after just six numbers (the next number and all subsequent numbers are 0).</p>

<p>Note that some sequences repeat in a more complex way; this one alternates back and forth between 576 and 3249:</p>

<pre>                Num  Middle  Square
                2245   24      576  
                 576   57     3249 
                3249   24      576  </pre>

<p>Your job is to tell Bessie the count of 'random numbers' that can be generated from a starting number before the sequence repeats a previously seen number. In the first case above, the answer is '6'. In the 'alternating' case, the answer is '3'.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the count of iterations through the middle square random number generator before a previous value is repeated</li>
</ul>

<p> </p>

