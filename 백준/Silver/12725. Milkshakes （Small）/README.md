# [Silver IV] Milkshakes (Small) - 12725 

[문제 링크](https://www.acmicpc.net/problem/12725) 

### 성능 요약

메모리: 115448 KB, 시간: 180 ms

### 분류

비트마스킹(bitmask), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>You own a milkshake shop. There are N different flavors that you can prepare, and each flavor can be prepared "malted" or "unmalted". So, you can make 2N different types of milkshakes.</p>

<p>Each of your customers has a set of milkshake types that they like, and they will be satisfied if you have at least one of those types prepared. At most one of the types a customer likes will be a "malted" flavor.</p>

<p>You want to make N batches of milkshakes, so that:</p>

<ul>
	<li>There is exactly one batch for each flavor of milkshake, and it is either malted or unmalted.</li>
	<li>For each customer, you make at least one milkshake type that they like.</li>
	<li>The minimum possible number of batches are malted.</li>
</ul>

<p>Find whether it is possible to satisfy all your customers given these constraints, and if it is, what milkshake types you should make.</p>

<p>If it is possible to satisfy all your customers, there will be only one answer which minimizes the number of malted batches.</p>

### 입력 

 <ul>
	<li>One line containing an integer <strong>C</strong>, the number of test cases in the input file.</li>
</ul>

<p>For each test case, there will be:</p>

<ul>
	<li>One line containing the integer <strong>N</strong>, the number of milkshake flavors.</li>
	<li>One line containing the integer <strong>M</strong>, the number of customers.</li>
	<li><strong>M</strong> lines, one for each customer, each containing:
	<ul>
		<li>An integer <strong>T</strong> >= 1, the number of milkshake types the customer likes, followed by</li>
		<li><strong>T</strong> pairs of integers "<strong>X Y</strong>", one for each type the customer likes, where <strong>X</strong> is the milkshake flavor between <strong>1</strong> and <strong>N</strong> inclusive, and <strong>Y</strong> is either 0 to indicate unmalted, or 1 to indicated malted. Note that:
		<ul>
			<li>No pair will occur more than once for a single customer.</li>
			<li>Each customer will have at least one flavor that they like (T >= 1).</li>
			<li>Each customer will like at most one malted flavor. (At most one pair for each customer has Y = 1).</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

<p>All of these numbers are separated by single spaces.</p>

<p>Limits</p>

<ul>
	<li>C = 100</li>
	<li>1 <= N <= 10</li>
	<li>1 <= M <= 100</li>
</ul>

### 출력 

 <ul>
	<li><strong>C</strong> lines, one for each test case in the order they occur in the input file, each containing the string "Case #<strong>X</strong>: " where <strong>X</strong> is the number of the test case, starting from 1, followed by:
	<ul>
		<li>The string "<strong>IMPOSSIBLE</strong>", if the customers' preferences cannot be satisfied; <strong>OR</strong></li>
		<li><strong>N</strong> space-separated integers, one for each flavor from <strong>1</strong> to <strong>N</strong>, which are 0 if the corresponding flavor should be prepared unmalted, and 1 if it should be malted.</li>
	</ul>
	</li>
</ul>

