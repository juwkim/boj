# [Unrated] Base K - 5228 

[문제 링크](https://www.acmicpc.net/problem/5228) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

수학(math), 구현(implementation)

### 문제 설명

<p>We are now used to the decimal positional notation for representing numbers, the modern version of which only dates back to the 9<sup>th</sup> century. In this notation we use 10 digits, from 0 to 9, to represent a number. However there is nothing special about 10, and we can just as easily use any other base to represent numbers. For example, in base-2 (binary) notation, we only use 2 digits, 0 and 1, whereas in base-16 (hexadecimal) notation, we use 15 digits: 0-9, a, b, c, d, e, f (the last 6 representing the digits ten, eleven, twelve, thirteen, fourteen, and fifteen); both these notations are commonly used by computers. In fact, several other bases are commonly seen in history: base-60 (used by ancient Babylonians), base-13 (used by Mayans), base-20 (Aztecs and Mayans, and possibly old Europe), base-27 (Telefol language and the Oksapmin language), and so on.</p>

<p>More generally, a base-$k$ representation uses $k$ digits: $0$ to $k - 1$. Given a number $n$ represented in base-$k$ as $a_3a_2a_1a_0$, where $a_3$, $a_2$, $a_1$, $a_0$ are digits, we have that: $$n = (a_3a_2a_1a_0)_k = a_3 \times k^3 + a_2 \times k^2 + a_1 \times k^1 + a_0 \times k^0$$</p>

<p>Here we use the subscript $k$ to denote that the number is being written in base-$k$.</p>

<p>For example,</p>

<ul>
	<li>$465_7 = 4 \times 7^2 + 6 \times 7^1 + 5 \times 7^0 = 243_{10}$</li>
	<li>$46E_{16} = 4 \times 16^2 + 6 \times 16^1 + 14 \times 16^0 = 1134_{10}$ (recall $E$ represents the number fourteen in base-16)</li>
</ul>

<p>Our use of decimal notation is likely based on it being easier to count up to 10 using fingers. However, programs have no such restriction. When Sam arrives on the Grid world, he discovers that the programs use arbitrary bases to communicate numbers to each other. Sam, not really being a program, has serious trouble with this, and practices arithmetic in arbitrary bases as much as he can. For example, when he sees any two numbers written together, call them $n$ and $k$, he times how long it takes him to decide whether base-$k$ representation of n contains all digits from $0$ to $k − 1$.</p>

<p>For example, base-3 representation of fifteen $(15_{10})$ is $120_3$: $$120_3 = 1 \times 3^2 + 2 \times 3^1 + 0 \times 3^0 = 9 + 6 + 0 = 15_{10}$$</p>

<p>which contains all 3 digits. In comparison, base-4 representation of eighteen $(18_{10})$ is $102_4$: $$102_4 = 1 \times 4^2 + 0 \times 4^1 + 2 \times 4^0 = 16 + 0 + 12 = 18_{10}$$</p>

<p>does not contain all 4 digits (it only contains 0, 1, and 2).</p>

<p>You are to write a program to help Sam verify his answers, i.e., given two numbers $n$ and $k$, you are to decide if base-$k$ representation of $n$ contains all digits from $0$ to $k - 1$. Note that the digit 0 must appear somewhere in the middle of the number; so the number 123456789 in base-10 representation does NOT contain all digits (it only contains 1-9, but no 0, even though we can also write the number as 0123456789).</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case, i.e., two numbers $n$ and $k$, in that order. Assume that $2 \le k \le 30$, and $0 \le n < 2^{30}$.</p>

### 출력 

 <p>The output is shown with an extra blank line so that each test case input is aligned with the output; that blank line should not be present in the actual output.</p>

