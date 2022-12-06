# [Silver V] Plumbing the Pond - 6107 

[문제 링크](https://www.acmicpc.net/problem/6107) 

### 성능 요약

메모리: 114328 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Bessie's drinks water from a pond in the northwest part of the farm. It has an interesting bottom in that it is full of little hills and valleys. She wonders how deep it is.</p>

<p>She trolls across the pond in her little boat with a very old radar set that tends to have spurious readings. She knows the deepest part is relatively flat and has decided that she'll believe the largest depth number only if it is verified by the fact that the same depth appears in an adjacent reading.</p>

<p>The pond is modeled as an R x C (1 <= R <= 50; 1 <= C <= 50) grid of (positive integer) depth readings D_rc (0 <= D_rc <= 1,000,000); some readings might be 0 -- those are not part of the pond. A depth reading of 10 means "depth of 10".</p>

<p>Find the greatest depth that appears in at least two 'adjacent' readings (where 'adjacent' means in any of the potentially eight squares that border a square on each of its sides and its diagonals). She knows the pond has at least one pair of positive, adjacent readings.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: R and C</li>
	<li>Lines 2..R+1: Line i+1 contains C space-separated integers that represent the depth of the pond across row i: D_rc</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the depth of the pond determined by following Bessie's rules.</li>
</ul>

<p> </p>

