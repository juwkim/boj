# [Bronze II] Star Arrangements - 15121 

[문제 링크](https://www.acmicpc.net/problem/15121) 

### 성능 요약

메모리: 28776 KB, 시간: 92 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>The recent vote in Puerto Rico favoring United States statehood has made flag makers very excited. An updated flag with 51 stars rather than the current one with 50 would cause a huge jump in U.S. flag sales. The current pattern for 50 stars is five rows of 6 stars, interlaced with four offset rows of 5 stars. The rows alternate until all stars are represented.</p>

<pre>* * * * * *
 * * * * *
* * * * * *
 * * * * *
* * * * * *
 * * * * *
* * * * * *
 * * * * *
* * * * * *</pre>

<p>This pattern has the property that adjacent rows differ by no more than one star. We represent this star arrangement compactly by the number of stars in the first two rows: 6,5.</p>

<p>A 51-star flag that has the same property can have three rows of 9 stars, interlaced with three rows of 8 stars (with a compact representation of 9,8). Conversely, if a state were to leave the union, one appealing representation would be seven rows of seven stars (7,7).</p>

<p>A flag pattern is visually appealing if it satisfies the following conditions:</p>

<ul>
	<li>Every other row has the same number of stars.</li>
	<li>Adjacent rows differ by no more than one star.</li>
	<li>The first row cannot have fewer stars than the second row.</li>
</ul>

<p>Your team sees beyond the short-term change to 51 for the U.S. flag. You want to corner the market on flags for any union of three or more states. Given the number S of stars to draw on a flag, find all possible visually appealing flag patterns.</p>

### 입력 

 <p>The input consists of a single line containing the integer S (3 ≤ S ≤ 32,767).</p>

### 출력 

 <p>On the first line, print S, followed by a colon. Then, for each visually appealing flag of S stars, print its compact representation, one per line.</p>

<p>This list of compact representations should be printed in increasing order of the number of stars in the first row; if there are ties, print them in order of the number of stars in the second row. The cases 1-by-S and S-by-1 are trivial, so do not print those arrangements.</p>

<p>The compact representations must be printed in the form “x,y”, with exactly one comma between x and y and no other characters.</p>

