# [Bronze I] Alignment of the Planets - 26996 

[문제 링크](https://www.acmicpc.net/problem/26996) 

### 성능 요약

메모리: 115136 KB, 시간: 772 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry)

### 문제 설명

<p>Actually, this problem is about alignment of N (1 ≤ N ≤ 770) cows numbered 1..N who are grazing in their field that is about 15,000x15,000 units. Their grazing locations all fall on integer coordinates in a standard x,y scheme (coordinates are in the range 0..15,000).</p>

<p>Bessie looks up and notices that she is exactly lined up with Sara and Julie. She wonders how many groups of three aligned cows exist within the field.</p>

<p>Given the locations of all the cows (no two cows occupy the same location), figure out all sets of three cows are exactly collinear. Keep track of the sets, sorting the cows in each set by their ID number, lowest first. Then sort the sets by the three ID numbers (lowest first), breaking ties by examining the second and third ID numbers.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, N</li>
	<li>Lines 2..N+1: Line i+1 describes cow i's location with two space-separated integers that are her x and y coordinates</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of sets of three cows that are exactly collinear. A set of four collinear cows would, of course, result in four sets of three collinear cows.</li>
	<li>Lines 2..?: Each line contains three space-separated integers that are the cow ID numbers of three collinear cows. The lines are sorted as specified above. This output section is empty if no collinear sets exist.</li>
</ul>

