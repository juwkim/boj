# [Bronze II] String LD - 9377 

[문제 링크](https://www.acmicpc.net/problem/9377) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>Stringld (left delete) is a function that gets a string and deletes its leftmost character (for instance Stringld(“acm”) returns “cm”).</p>

<p>You are given a list of distinct words, and at each step, we apply stringld on every word in the list. Write a program that determines the number of steps that can be applied until at least one of the conditions become true:</p>

<ol>
	<li>A word becomes empty string, or</li>
	<li>a duplicate word is generated.</li>
</ol>

<p>For example, having the list of words aab, abac, and caac, applying the function on the input for the first time results in ab, bac, and aac. For the second time, we get b, ac, and ac. Since in the second step, we have two ac strings, the condition 2 is true, and the output of your program should be 1. Note that we do not count the last step that has resulted in duplicate string. More examples are found in the sample input and output section. </p>

### 입력 

 <p>There are multiple test cases in the input. The first line of each test case is n (1  n  100), the number of words. Each of the next n lines contains a string of at most 100 lower case characters. The input terminates with a line containing 0.</p>

### 출력 

 <p>For each test case, write a single line containing the maximum number of stringld we can call.</p>

