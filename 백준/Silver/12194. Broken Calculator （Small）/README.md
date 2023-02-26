# [Silver IV] Broken Calculator (Small) - 12194 

[문제 링크](https://www.acmicpc.net/problem/12194) 

### 성능 요약

메모리: 113112 KB, 시간: 132 ms

### 분류

Empty

### 문제 설명

<p>Alice is a smart student who is very good at math. She is attending a math class. In this class, the teacher is teaching the students how to use a calculator. The teacher will tell an integer to all of the students, and the students must type that exact number into their calculators. If someone fails to type the number, he or she will be punished for failing such an easy task!</p>

<p>Unfortunately, at the beginning of the class, Alice finds that her calculator is broken! She finds that some of the number buttons are totally broken, and only the "multiply" and "equals" operator buttons are available to use. So she can only use these buttons to get the number quickly.</p>

<p>For instance, the teacher may say the number "60", while Alice's calculator can only type "1", "2" and "5". She could push the following buttons:</p>

<ul>
	<li>Button "15" (2 clicks)</li>
	<li>Button "multiply" (1 click)</li>
	<li>Button "2" (1 click)</li>
	<li>Button "multiply" (1 click)</li>
	<li>Button "2" (1 click)</li>
	<li>Button "equals" (1 click)</li>
</ul>

<p>This method requires 7 button clicks. However, if Alice uses "12*5=", only 5 clicks are needed. Of course Alice wants to get the integer as fast as possbile, so she wants to minimize the number of button clicks. Your task is to help her find a way to get the required number quickly.</p>

### 입력 

 <p>The first line of the input gives a number <strong>T</strong>, the number of integers the teacher says. <strong>T</strong> test cases follow.</p>

<p>Each case contains two lines. The first line contains ten numbers each of which is only 0 or 1. the <strong>i</strong>th number (starting from 0) is "1" if the number <strong>i</strong> can be clicked, or "0" if it is broken. The second line contains only one number <strong>X</strong>, the integer the teacher tells everyone.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">X</strong><span style="line-height:1.6em"> ≤ 100.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of button clicks needed, or "Impossible" if it is not possible to produce the number.</p>

