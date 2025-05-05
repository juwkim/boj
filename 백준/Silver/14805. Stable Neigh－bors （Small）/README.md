# [Silver I] Stable Neigh-bors (Small) - 14805 

[문제 링크](https://www.acmicpc.net/problem/14805) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

해 구성하기

### 제출 일자

2025년 5월 6일 00:37:22

### 문제 설명

<p>You are lucky enough to own <strong>N</strong> pet unicorns. Each of your unicorns has either one or two of the following kinds of hairs in its mane: red hairs, yellow hairs, and blue hairs. The color of a mane depends on exactly which sorts of colored hairs it contains:</p>

<ul>
	<li>A mane with only one color of hair appears to be that color. For example, a mane with only blue hairs is blue.</li>
	<li>A mane with red and yellow hairs appears orange.</li>
	<li>A mane with yellow and blue hairs appears green.</li>
	<li>A mane with red and blue hairs appears violet.</li>
</ul>

<p>You have <strong>R</strong>, <strong>O</strong>, <strong>Y</strong>, <strong>G</strong>, <strong>B</strong>, and <strong>V</strong> unicorns with red, orange, yellow, green, blue, and violet manes, respectively.</p>

<p>You have just built a circular stable with <strong>N</strong> stalls, arranged in a ring such that each stall borders two other stalls. You would like to put exactly one of your unicorns in each of these stalls. However, unicorns need to feel rare and special, so no unicorn can be next to another unicorn that shares at least one of the hair colors in its mane. For example, a unicorn with an orange mane cannot be next to a unicorn with a violet mane, since both of those manes have red hairs. Similarly, a unicorn with a green mane cannot be next to a unicorn with a yellow mane, since both of those have yellow hairs.</p>

<p>Is it possible to place all of your unicorns? If so, provide any one arrangement.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each consists of one line with seven integers: <strong>N</strong>, <strong>R</strong>, <strong>O</strong>, <strong>Y</strong>, <strong>G</strong>, <strong>B</strong>, and <strong>V</strong>.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>3 ≤ <strong>N</strong> ≤ 1000.</li>
	<li><strong>R</strong> + <strong>O</strong> + <strong>Y</strong> + <strong>G</strong> + <strong>B</strong> + <strong>V</strong> = <strong>N</strong>.</li>
	<li>0 ≤ Z for each Z in {<strong>R</strong>, <strong>O</strong>, <strong>Y</strong>, <strong>G</strong>, <strong>B</strong>, <strong>V</strong>}.</li>
	<li><strong>O</strong> = <strong>G</strong> = <strong>V</strong> = 0. (Each unicorn has only one hair color in its mane.)</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is <code>IMPOSSIBLE</code> if it is not possible to place all the unicorns, or a string of <strong>N</strong> characters representing the placements of unicorns in stalls, starting at a point of your choice and reading clockwise around the circle. Use <code>R</code> to represent each unicorn with a red mane, <code>O</code> to represent each unicorn with an orange mane, and so on with <code>Y</code>, <code>G</code>, <code>B</code>, and <code>V</code>. This arrangement must obey the rules described in the statement above.</p>

<p>If multiple arrangements are possible, you may print any of them.</p>

