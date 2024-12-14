# [Silver II] Bronze Lilypad Pond - 6229 

[문제 링크](https://www.acmicpc.net/problem/6229) 

### 성능 요약

메모리: 113500 KB, 시간: 120 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 15일 04:09:23

### 문제 설명

<p>Farmer John has installed a beautiful pond for his cows' esthetic enjoyment and exercise. The rectangular pond has been partitioned into square cells of M rows and N columns (1 <= M <= 30; 1 <= N <= 30). Some of the cells have astonishingly sturdy lilypads; others have rocks; the remainder are just beautiful, cool, blue water.</p>

<p>Bessie is practising her ballet moves by jumping from one lilypad to another and is currently located at one of the lilypads (see the input data for the location's specifier). She wants to travel to another lilypad in the pond by jumping from one lilypad to another. She can jump neither into the water nor onto a rock.</p>

<p>Surprising only to the uninitiated, Bessie's jumps between lilypads always appear as a sort of chess-knight's move: move M1 (1 <= M1 <= 30) 'squares' in one direction and then M2 (1 <= M2 <= 30; M1 != M2) more in an orthogonal direction (or perhaps M2 in one direction and then M1 in an orthogonal direction). Bessie sometimes might have as many as eight choices for her jump.</p>

<p>Given the pond layout and the format of Bessie's jumps, determine the smallest number of leaps that Bessie must make to move from her starting location to her final destination, a feat which is always possible for the given test data.</p>

### 입력 

 <ul>
	<li>Line 1: Four space-separated integers: M, N, M1, and M2</li>
	<li>Lines 2..M+1: Line i+1 describes row i of the pond using N space-separated integers with these values: 0 indicates empty water; 1 indicates a lilypad; 2 indicates a rock; 3 indicates the lilypad Bessie upon which she starts; 4 indicates the lilypad that is Bessie's destination.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the minimum number of jumps between lilypads that Bessie must make to travel from her starting place to her destination.</li>
</ul>

