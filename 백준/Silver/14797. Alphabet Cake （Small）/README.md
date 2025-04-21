# [Silver I] Alphabet Cake (Small) - 14797 

[문제 링크](https://www.acmicpc.net/problem/14797) 

### 성능 요약

메모리: 109412 KB, 시간: 88 ms

### 분류

백트래킹, 브루트포스 알고리즘, 그리디 알고리즘

### 제출 일자

2025년 4월 21일 12:57:20

### 문제 설명

<p>You are catering a party for some children, and you are serving them a cake in the shape of a grid with <strong>R</strong> rows and <strong>C</strong> columns. Your assistant has started to decorate the cake by writing every child's initial in icing on exactly one cell of the cake. Each cell contains at most one initial, and since no two children share the same initial, no initial appears more than once on the cake.</p>

<p>Each child wants a single rectangular (grid-aligned) piece of cake that has their initial and no other child's initial(s). Can you find a way to assign every blank cell of the cake to one child, such that this goal is accomplished? It is guaranteed that this is always possible. There is no need to split the cake evenly among the children, and one or more of them may even get a 1-by-1 piece; this will be a valuable life lesson about unfairness.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each begins with one line with two integers <strong>R</strong> and <strong>C</strong>. Then, there are <strong>R</strong> more lines of <strong>C</strong>characters each, representing the cake. Each character is either an uppercase English letter (which means that your assistant has already added that letter to that cell) or <code>?</code>(which means that that cell is blank).</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>There is at least one letter in the input grid.</li>
	<li>No letter appears in more than one cell in the input grid.</li>
	<li>It is guaranteed that at least one answer exists for each test case.</li>
	<li>1 ≤ <strong>R</strong> ≤ 12.</li>
	<li>1 ≤ <strong>C</strong> ≤ 12.</li>
	<li><strong>R</strong> × <strong>C</strong> ≤ 12.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x:</code> and nothing else. Then output <strong>R</strong>more lines of <strong>C</strong> characters each. Your output grid must be identical to the input grid, but with <em>every</em> <code>?</code> replaced with an uppercase English letter, representing that that cell appears in the slice for the child who has that initial. You may not add letters that did not originally appear in the input. In your grid, for each letter, the region formed by all the cells containing that letter must be a single grid-aligned rectangle.</p>

<p>If there are multiple possible answers, you may output any of them.</p>

