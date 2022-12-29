# [Bronze I] Computation - Task 1 - 25745 

[문제 링크](https://www.acmicpc.net/problem/25745) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Given a task, you should write a program that solves the task using the instructions below. Let $x_t$ denote the result of the $t$-th instruction. The permitted instructions, the syntax, and the result $x_t$ are given below:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Name</th>
			<th>Operator</th>
			<th>Parameters</th>
			<th>Effects</th>
		</tr>
		<tr>
			<td>Input</td>
			<td><code>I</code></td>
			<td>N/A</td>
			<td>Read a real number from the terminal and make the number $x_t$</td>
		</tr>
		<tr>
			<td>Output</td>
			<td><code>O</code></td>
			<td>$i$</td>
			<td>Print $x_i$ to the terminal, and $x_t = x_i$</td>
		</tr>
		<tr>
			<td>Addition</td>
			<td><code>+</code></td>
			<td>$i \quad j$</td>
			<td>$x_t = x_i + x_j$</td>
		</tr>
		<tr>
			<td>Adding constant</td>
			<td><code>C</code></td>
			<td>$i \quad c$</td>
			<td>$x_t = x_i +c$</td>
		</tr>
		<tr>
			<td>Negate</td>
			<td><code>-</code></td>
			<td>$i$</td>
			<td>$x_t = -x_i $</td>
		</tr>
		<tr>
			<td>Left shift</td>
			<td><code><</code></td>
			<td>$i \quad k$</td>
			<td>$x_t = x_i \cdot 2^k $</td>
		</tr>
		<tr>
			<td>Right shift</td>
			<td><code>></code></td>
			<td>$i \quad k$</td>
			<td>$x_t = x_i \cdot 2^{-k} $</td>
		</tr>
		<tr>
			<td>S</td>
			<td><code>S</code></td>
			<td>$i$</td>
			<td>$x_t = s(x_i) $</td>
		</tr>
		<tr>
			<td>Comparison</td>
			<td><code>P</code></td>
			<td>$i \quad j$</td>
			<td>$x_t = \left\{ \begin{array}{ll} -1 & \quad x_i < x_j \\ 0 & \quad x_i = x_j \\ 1 & \quad x_i > x_j \end{array} \right. $</td>
		</tr>
		<tr>
			<td>Max</td>
			<td><code>M</code></td>
			<td>$i \quad j$</td>
			<td>$x_t = \left\{ \begin{array}{ll} x_i & \quad x_i > x_j \\ x_j & \quad x_i \leq x_j \\ \end{array} \right. $</td>
		</tr>
		<tr>
			<td>Multiplication</td>
			<td><code>*</code></td>
			<td>$i \quad j$</td>
			<td>$x_i = x_i \cdot x_j$</td>
		</tr>
	</tbody>
</table>

<p>Here, the definition of $s(x)$ is given below where $e = 2.718281828459045\ldots$ is the base of natural logarithm:</p>

<p>$$\displaystyle s(x) = \frac{1}{1 + e^{-x}}.$$</p>

<p>Notice there is a penalty for using the <code>P</code>, <code>M</code>, and <code>*</code> operators. See details below in the "grading" section.</p>

<p>For each instruction, the parameters $i$ and $j$ must be smaller than the current instruction number $t$. The instructions are executed in the order, one by one.</p>

<p>The operations have finite precision: in particular, <em>the results are only accurate up to 90 digits after the decimal point and the rest will be rounded</em>. Similarly, the argument $c$ to the adding constant instruction can have at most 90 digits in its decimal part.</p>

<p>For left shift and right shift instructions, $k$ must be a non-negative integer not exceeding 10000.</p>

<p>The ten tasks are given below:</p>

<ul>
	<li>Task 1: Given $a,b$ where $|a|, |b| \leq 10^9$ and $a,b$ have at most 9 digits in their decimal parts, compute $-2a-2b$.</li>
	<li>Task 2: Given $a$ where $|a| \leq 10^9$ and $a$ has at most 9 digits in its decimal part, compute $\frac{1}{1+e^{17a}}$.</li>
	<li>Task 3: Given $a$ where $|a| \leq 10^9$ and $a$ has at most 9 digits in its decimal part, compute $ \left\{ \begin{array}{ll} -1 & \quad a < 0\\ 0 & \quad a = 0\\ 1 & \quad a > 0 \end{array} \right. $.</li>
	<li>Task 4: Given $a$ where $|a| \leq 10^9$ and $a$ has at most 9 digits in its decimal part, compute the absolute value of $a$, $|a|$.</li>
	<li>Task 5: Given $a_1,\ldots,a_{32}$ where $a_1,\ldots,a_{32} \in \{0,1\}$, treat $a_1a_2 \cdots a_{32}$ as a binary number where $a_1$ is the most significant bit and $a_{32}$ is the least significant bit, compute the corresponding value (in base 10).</li>
	<li>Task 6: Given integer $a$ where $0 \leq a < 2^{32}$, output 32 integers denoting $a$ in base 2 representation. The most significant bit should be printed first and the least significant bit should be printed last. If $a$ has less than 32 bits in its binary representation, add leading 0s.</li>
	<li>Task 7: Given integers $a,b$ where $0 \leq a,b < 2^{32}$, compute the bitwise XOR of $a$ and $b$.</li>
	<li>Task 8: Given $a$ where $|a| \leq 10^9$ and $a$ has at most 9 digits in its decimal part, output $\frac{a}{10}$.</li>
	<li>Task 9: Given $a_1,\ldots,a_{16}$ where $|a_i| \leq 10^9$ and $a_i$ has at most 9 digits in its decimal part, print 16 real numbers representing the result of sorting $a_1,\ldots,a_{16}$ in ascending order.</li>
	<li>Task 10: Given integers $a,b,m$ where $0 \leq a,b < 2^{32}$, $1 \leq m < 2^{32}$, compute the remainder after dividing $a \times b$ by $m$ (i.e. compute $a \times b \bmod m$).</li>
</ul>

### 입력 

 Empty

### 출력 

 <p>The $i$-th line describes the $i$-th instruction: first, you should output a letter denoting the operation. Then output several (or zero) integers denoting the parameters to the operation. The operator and the parameters (and between parameters) should be separated by a single space.</p>

<p>You can output at most $10^4$ lines.</p>

