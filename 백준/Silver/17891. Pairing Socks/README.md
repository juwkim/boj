# [Silver IV] Pairing Socks - 17891 

[문제 링크](https://www.acmicpc.net/problem/17891) 

### 성능 요약

메모리: 144644 KB, 시간: 244 ms

### 분류

자료 구조, 스택

### 문제 설명

<p>Simone’s mother often complains about how Simone never helps with chores at home. In return, Simone often points out that many of the chores her mother assigns her are NP-complete to perform optimally (like cleaning the house, seating her little brothers around the dinner table in a conflict-free way, splitting the brothers’ Halloween loot in a fair manner and so on).</p>

<p>Being a computer scientist, her mother finds this a fair objection. Looking over her list of potential chores, she picked one she thinks should be easy to solve – pairing a number of different kinds of socks.</p>

<p>In the beginning, there are 2n socks stacked in a pile. To pair the socks, Simone can repeatedly make one of three moves:</p>

<ol>
	<li>Move the sock from the top of the original pile to the top of an auxiliary pile (which is originally empty).</li>
	<li>Move the sock from the top of the auxiliary pile to the top of the original pile.</li>
	<li>Pair the top socks from each pile together, if they are of the same type.</li>
</ol>

<p>Simone only has one auxiliary pile, for a total of two piles. There may be more than two socks of each type. In this case, Simone can pair them up however she wants.</p>

<p>Your task is to help Simone to determine the least number of moves she needs to pair the socks, if it is possible at all.</p>

### 입력 

 <p>The first line of input contains the integer n (1 ≤ n ≤ 10<sup>5</sup>) as described above. The next line contains 2n integers a<sub>1</sub>, . . . , a<sub>2n</sub> (1 ≤ a<sub>i</sub> ≤ 10<sup>9</sup> for each i), where a<sub>i</sub> denotes the type of sock number i. Initially, sock 1 is at the top of the pile and sock 2n is at the bottom.</p>

### 출력 

 <p>If Simone can pair all the socks, output the least number of moves she needs to do this. If it is impossible to do so, output “impossible” (without the quotes).</p>

