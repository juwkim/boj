# [Silver V] finitefunc - 25033 

[문제 링크](https://www.acmicpc.net/problem/25033) 

### 성능 요약

메모리: 114328 KB, 시간: 4 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p>A function whose domain is a finite set can be implemented using a Python dictionary. Let <code>D</code> be such a Python dictionary corresponding to the mathematical function $f\colon X\to Y$ where $X$ is a finite set. The value of $f$ at <code>x</code> is <code>D[x]</code> and the domain $X$ is the set of all keys of <code>D</code>. Return the range $\{f(x):x\in X\}$, in Python set.</p>

<p>Write a function <u><code>finitefunc</code></u>:</p>

<ul>
	<li>input parameter: a <code>dict</code>-type object <code>D</code>

	<ul>
		<li><code>D</code> has at most 1000 keys.</li>
		<li>Every key and value of <code>D</code> is an <code>int</code>-type object whose absolute value is less than or equal to $1000$.</li>
	</ul>
	</li>
	<li>return value: the <code>set</code>-type object <code>S</code> representing the range of the function
	<ul>
		<li>Every element of <code>S</code> should be an <code>int</code>-type object.</li>
	</ul>
	</li>
</ul>

### 입력 

 Empty

### 출력 

 Empty

