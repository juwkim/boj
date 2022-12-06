# [Silver V] DNA Sequencing - 6021 

[문제 링크](https://www.acmicpc.net/problem/6021) 

### 성능 요약

메모리: 115424 KB, 시간: 144 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Farmer John is studying the geneology of his herd. He has M bulls (1 <= M <= 20) and F cows (1 <= F <= 20). He doesn't know, though, which bovines are potential descendants of which other bovines.</p>

<p>Farmer John does know the unique DNA sequence DNA_i of each and every cow and bull on his farm. DNA_i has length 25 characters and contains only upper-case letters 'A', 'C', 'G', and 'T'. He wants to determine which bovines could possibly be children of which pairs of cows and bulls.</p>

<p>Help Farmer John make this determination. For each pair of a cow and a bull, print how many of FJ's other bovines could possibly be their children. A bovine can be a child of a given cow and bull if</p>

<ol>
	<li>it is not either of its parents (that is, a cow cannot be its own mother and a bull cannot be its own father)</li>
	<li>each position in its DNA sequence matches at least one of the characters in the same position in the two parent sequences</li>
</ol>

<p>So for example, 'abc' could come from pair ('axx', 'xbc'), but not from the pair ('aaa', 'bbb').</p>

<p>Consider three bulls and two cows with these DNA sequences:</p>

<pre>       Bull 1: GTTTTTTTTTTTTTTTTTTTTTTTT
       Bull 2: AATTTTTTTTTTTTTTTTTTTTTTT
       Bull 3: GATTTTTTTTTTTTTTTTTTTTTTT
       Cow 1:  TTTTTTTTTTTTTTTTTTTTTTTTT
       Cow 2:  ATTTTTTTTTTTTTTTTTTTTTTTT</pre>

<p>Bull 2 and cow 1 could be the parents of cow 2:</p>

<pre>       Bull 2: AATTTTTTTTTTTTTTTTTTTTTTT
       Cow 1:  TTTTTTTTTTTTTTTTTTTTTTTTT
       Cow 2:  ATTTTTTTTTTTTTTTTTTTTTTTT</pre>

<p>since cow 2's first letter 'A' could be from Bull 2; cow 2's second letter 'T' could come from cow 1; the remainder of the letters could come from either parent.</p>

<p>Your goal is to create a matrix of the count of possible offspring of each pairing of bulls and cows. </p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: M and F</li>
	<li>Lines 2..M+1: Line i+1 gives the DNA sequence of bull i: DNA_i</li>
	<li>Lines M+2..M+F+1: Line j+M+1 gives the DNA sequence of cow j: DNA_j</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..M: Line i: F space-separated integers. The jth integer is the number of bovines that could be children of the ith bull and jth cow.</li>
</ul>

<p> </p>

