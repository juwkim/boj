# [Bronze II] Robot Rock Band (Small) - 12044 

[문제 링크](https://www.acmicpc.net/problem/12044) 

### 성능 요약

메모리: 115408 KB, 시간: 344 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>You're the manager of Xorbitant, the world's first robot rock band. There will be four positions in the band, and there are <strong>N</strong> robots auditioning for each position. (No robot is auditioning for more than one position.) Every robot has a number, and multiple robots might have the same number, just as two people can have the same name.</p>

<p>You know from market research that your robot audiences won't care how well the robot band members make music, how handsome they are, or what scandalous things the tabloids say about them. Instead, the audience will be checking to see whether the four members' numbers, when bitwise XORed together, equal a certain trendy number <strong>K</strong>.</p>

<p>How many different sets of four robots (one for each position) is it possible to choose so that the band will have this property? More specifically, given four lists A, B, C, D containing <strong>N</strong> numbers each, how many ways are there to choose one number <em>a</em> from list A, one number <em>b</em> from list B, and so on, such that <em>a</em>^<em>b</em>^<em>c</em>^<em>d</em> = <strong>K</strong>? (Here ^ represents the bitwise XOR operation.)</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each case begins with one line with two space-separated integers, <strong>N</strong> and <strong>K</strong>, as described above. Then, four more lines follow. Each has <strong>N</strong> space-separated integers and represents the ID numbers of the robots auditioning for a certain position in the band.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 10.</li>
	<li>0 ≤ <strong>K</strong> ≤ 10<sup>9</sup>.</li>
	<li>0 ≤ all robot numbers ≤ 10<sup>9</sup>.</li>
	<li>1 ≤ <strong>N</strong> ≤ 50.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of different bands that meet the conditions.</p>

