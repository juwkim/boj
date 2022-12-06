# [Silver V] Linden Mayor System - 24784 

[문제 링크](https://www.acmicpc.net/problem/24784) 

### 성능 요약

메모리: 114652 KB, 시간: 116 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p><img alt="" src="" style="width: 240px; height: 240px; float: right;">Aristid is the mayor of a town called Linden. He and the townsfolk love fractals. One day, Aristid decides to genetically alter trees so that they have mathematically pleasing structures. It turns out that the people of Linden will support this idea only if the trees are sufficiently "tree-like." So Aristid came up with the following system to generate realistic looking trees. Since he's a little vain, he decided to call it the Linden Mayor System.</p>

<p>Start with a sequence of letters $S_0$. This is the seed that will be used to generate the rest of the tree. Next define some rules to model the branching behavior of the tree. A rule will have the form $x \rightarrow y$, indicating that the letter $x$ will be replaced with the sequence $y$. By applying these rules to $S_0$, the new sequence $S_1$ is created. These rules can be applied over and over to produce new sequences.  In general, to create $S_{n+1}$ from $S_n$, replace all the letters in sequence $S_n$ according to the rules. Some letters may not have a rule associated with them.  Such <em>terminal</em> letters are not replaced.</p>

<p>As an example, consider the starting sequence A with rules: A $\rightarrow$ AB and B $\rightarrow$ A. The first four iterations are as follows:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>$S_0$:</td>
			<td>A</td>
			<td>Starting sequence.</td>
		</tr>
		<tr>
			<td>$S_1$:</td>
			<td>AB</td>
			<td>A is replaced with AB by rule A $\rightarrow$ AB. Note that rule B $\rightarrow$ A couldn't be applied.</td>
		</tr>
		<tr>
			<td>$S_2$:</td>
			<td>ABA</td>
			<td>Again, A is replaced by AB but B is replaced with A (rule B $\rightarrow$ A).</td>
		</tr>
		<tr>
			<td>$S_3$:</td>
			<td>ABAAB</td>
			<td>Keep applying rule A $\rightarrow$ AB for A's and rule B $\rightarrow$ A for B's...</td>
		</tr>
		<tr>
			<td>$S_4$:</td>
			<td>ABAABABA</td>
			<td>This is the resulting sequence after four iterations.</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The first line will contain two positive integers: $0 \leq n \leq 26$ and $0 \leq m \leq 5$.  Following this will be $n$ lines defining the rules for a Linden Mayor System. Each line is of the form: $x$ <code>-></code> $y$, indicating that $x$ is replaced by $y$. $x$ and $y$ will contain only uppercase letters from A to Z, and the length of $y$ is guaranteed to be at most five.  The last line will contain the starting sequence $S_0$ which will be no longer than $30$ characters and will contain only uppercase letters from A to Z.</p>

### 출력 

 <p>Output the resulting sequence $S_m$ which is produced after $m$ iterations.</p>

