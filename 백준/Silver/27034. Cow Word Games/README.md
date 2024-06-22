# [Silver III] Cow Word Games - 27034 

[문제 링크](https://www.acmicpc.net/problem/27034) 

### 성능 요약

메모리: 115260 KB, 시간: 216 ms

### 분류

구현

### 제출 일자

2024년 6월 23일 02:08:16

### 문제 설명

<p>Tired of being teased by the other farm animals for their poor vocabulary, Farmer John's cows have stolen a word game from FJ's house to use for practice.  In this particular word game, each cow receives a set of N (1 ≤ N ≤ 100) not necessarily unique uppercase letters (for example: 'V', 'B', 'O', 'E', 'I', 'N', 'O').  Each letter has a certain specified point value, and each cow's goal is to form a valid word using a subset of her letters worth the maximum number of points.  For example, if every letter is worth 1 point, the maximum number of points one can receive from the letters above is 6, using the word 'BOVINE'.</p>

<p>The cows have also managed to steal a dictionary containing M (1 ≤ M ≤ 10,000) words from FJ's house, so they can check whether or not certain words are valid.  Please help his cows compute the best possible words they can form based on the letters they receive.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, N and M (1 ≤ M ≤ 10000).</li>
	<li>Lines 2..27: Each of these 26 lines contains a positive integer giving the number of points for a letter of the alphabet. The first of these lines corresponds to 'A'; the last corresponds to 'Z'.</li>
	<li>Lines 28..N+27: These N lines contain the letters received by a cow playing the game.   Each line contains a single uppercase letter.</li>
	<li>Lines N+28..N+M+27: These M lines each contain a word from the dictionary.  Each word consists of at most N uppercase letters.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer, specifying the maximum number of points we can  receive.  If no valid words in the dictionary can be formed, output -1.</li>
</ul>

