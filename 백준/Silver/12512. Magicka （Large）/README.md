# [Silver IV] Magicka (Large) - 12512 

[문제 링크](https://www.acmicpc.net/problem/12512) 

### 성능 요약

메모리: 115140 KB, 시간: 164 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 구현(implementation), 시뮬레이션(simulation), 스택(stack), 문자열(string)

### 문제 설명

<p>As a wizard, you can <strong>invoke</strong> eight elements, which are the "base" elements. Each base element is a single character from {Q, W, E, R, A, S, D, F}. When you invoke an element, it gets appended to your <strong>element list</strong>. For example: if you invoke W and then invoke A, (we'll call that "invoking WA" for short) then your element list will be [W, A].</p>

<p>We will specify pairs of base elements that <strong>combine</strong> to form non-base elements (the other 18 capital letters). For example, Q and F might combine to form T. If the two elements from a pair appear at the end of the element list, then both elements of the pair will be immediately removed, and they will be replaced by the element they form. In the example above, if the element list looks like [A, Q, F] or [A, F, Q] at any point, it will become [A, T].</p>

<p>We will specify pairs of base elements that are <strong>opposed</strong> to each other. After you invoke an element, if it isn't immediately combined to form another element, and it is opposed to something in your element list, then your whole element list will be cleared.</p>

<p>For example, suppose Q and F combine to make T. R and F are opposed to each other. Then invoking the following things (in order, from left to right) will have the following results:</p>

<ul>
	<li>QF → [T] (Q and F combine to form T)</li>
	<li>QEF → [Q, E, F] (Q and F can't combine because they were never at the end of the element list together)</li>
	<li>RFE → [E] (F and R are opposed, so the list is cleared; then E is invoked)</li>
	<li>REF → [] (F and R are opposed, so the list is cleared)</li>
	<li>RQF → [R, T] (QF combine to make T, so the list is not cleared)</li>
	<li>RFQ → [Q] (F and R are opposed, so the list is cleared)</li>
</ul>

<p>Given a list of elements to invoke, what will be in the element list when you're done?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each test case consists of a single line, containing the following space-separated elements in order:</p>

<p>First an integer <strong>C</strong>, followed by <strong>C</strong> strings, each containing three characters: two base elements followed by a non-base element. This indicates that the two base elements combine to form the non-base element. Next will come an integer <strong>D</strong>, followed by <strong>D</strong> strings, each containing two characters: two base elements that are opposed to each other. Finally there will be an integer <strong>N</strong>, followed by a single string containing <strong>N</strong> characters: the series of base elements you are to invoke. You will invoke them in the order they appear in the string (leftmost character first, and so on), one at a time.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>Each pair of base elements may only appear together in one combination, though they may appear in a combination and also be opposed to each other.</li>
	<li>No base element may be opposed to itself.</li>
	<li>Unlike in the computer game Magicka, there is no limit to the length of the element list.</li>
	<li>0 ≤ <strong>C</strong> ≤ 36.</li>
	<li>0 ≤ <strong>D</strong> ≤ 28.</li>
	<li>1 ≤ <strong>N</strong> ≤ 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is a list in the format "[e<sub>0</sub>, e<sub>1</sub>, ...]" where e<sub>i</sub> is the i<sup>th</sup> element of the final element list. Please see the sample output for examples.</p>

