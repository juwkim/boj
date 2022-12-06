# [Silver V] Blue Jeans - 4542 

[문제 링크](https://www.acmicpc.net/problem/4542) 

### 성능 요약

메모리: 115208 KB, 시간: 144 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>The Genographic Project is a research partnership between IBM and The National Geographic Society that is analyzing DNA from hundreds of thousands of contributors to map how the Earth was populated.</p>

<p>As an IBM researcher, you have been tasked with writing a program that will find commonalities amongst given snippets of DNA that can be correlated with individual survey information to identify new genetic markers.</p>

<p>A DNA base sequence is noted by listing the nitrogen bases in the order in which they are found in the molecule. There are four bases: adenine (A), thymine (T), guanine (G), and cytosine (C). A 6-base DNA sequence could be represented as TAGACC.</p>

<p>Given a set of DNA base sequences, determine the longest series of bases that occurs in all of the sequences.</p>

### 입력 

 <p>Input to this problem will begin with a line containing a single integer n indicating the number of datasets. Each dataset consists of the following components:</p>

<ol>
	<li>A single positive integer m (2 <= m <= 10) indicating the number of base sequences in this dataset.</li>
	<li>m lines each containing a single base sequence consisting of 60 bases.</li>
</ol>

### 출력 

 <p>For each dataset in the input, output the longest base subsequence common to all of the given base sequences. If the longest common subsequence is less than three bases in length, display the string "no significant commonalities" instead. If multiple subsequences of the same longest length exist, output only the subsequence that comes first in alphabetical order.</p>

