# [Silver II] Selfish Grazing - 6011 

[문제 링크](https://www.acmicpc.net/problem/6011) 

### 성능 요약

메모리: 117656 KB, 시간: 156 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 2월 6일 23:10:38

### 문제 설명

<p>Each of Farmer John's N (1 <= N <= 50,000) cows likes to graze in a certain part of the pasture, which can be thought of as a large one-dimeensional number line. Cow i's favorite grazing range starts at location S_i and ends at location E_i (1 <= S_i < E_i; S_i < E_i <= 100,000,000).</p>

<p>Most folks know the cows are quite selfish; no cow wants to share any of its grazing area with another. Thus, two cows i and j can only graze at the same time if either S_i >= E_j or E_i <= S_j. FJ would like to know the maximum number of cows that can graze at the same time for a given set of cows and their preferences.</p>

<p>Consider a set of 5 cows with ranges shown below:</p>

<pre>  ... 1    2    3    4    5    6    7    8    9   10   11   12   13 ...
  ... |----|----|----|----|----|----|----|----|----|----|----|----|----
Cow 1:      <===:===>          :              :              :
Cow 2: <========:==============:==============:=============>:
Cow 3:          :     <====>   :              :              :
Cow 4:          :              :     <========:===>          :
Cow 5:          :              :     <==>     :              :</pre>

<p>These ranges represent (2, 4), (1, 12), (4, 5), (7, 10), and (7, 8), respectively.</p>

<p>For a solution, the first, third, and fourth (or fifth) cows can all graze at the same time. If the second cow grazed, no other cows could graze. Also, the fourth and fifth cows cannot graze together, so it is impossible for four or more cows to graze.</p>

### 입력 

 <ul>
	<li>Line 1: A  single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains the two space-separated integers: S_i and E_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer representing the maximum number of cows that can graze at once.</li>
</ul>

<p> </p>

