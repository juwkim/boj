# [Bronze II] George Boole - 13234 

[문제 링크](https://www.acmicpc.net/problem/13234) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>George Boole was an English mathematician, educator, philosopher who was born in 1815, 200 years ago. He was the first professor of mathematics at Queen's College, Cork (now University College Cork (UCC)) and is known as the inventor of boolean arithmetic: The field that is the basis of today’s computers.</p>

<p>In boolean arithmetic, instead of infinite numbers we only have 2 values: 0/1, true/false, yes/no, etc. We will use the values true and false in this problem. The two most common operations in boolean arithmetic are AND and OR.</p>

<p>The result of an AND operation is true only if both elements are true. Examples:</p>

<ul>
	<li>true AND true = true</li>
	<li>true AND false = false</li>
	<li>false AND false = false</li>
</ul>

<p>The result of an OR operation is true if any of the elements are true. Examples:</p>

<ul>
	<li>true OR true = true</li>
	<li>false OR false = false</li>
	<li>false OR true = true </li>
</ul>

<p>In this problem you’ll read one of such operations and write the correct result.</p>

### 입력 

 <p>Read a single line from the standard input. The line will contain three words with the format:</p>

<p>value1 operation value2. The fields value1 and value2 will be either true or false. The field operation will be either AND or OR.</p>

### 출력 

 <p>Print either true or false.</p>

